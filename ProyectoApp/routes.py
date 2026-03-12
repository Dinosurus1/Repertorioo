# routes.py
from flask import render_template, request, redirect, url_for, session, flash
from app import app, db
from models import Usuario
from email_utils import enviar_codigo_verificacion, enviar_codigo_recuperacion
import datetime

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        email = request.form['email'].strip().lower()
        password = request.form['password']
        
        # Validar que no exista el usuario
        usuario = Usuario.query.filter_by(email=email).first()
        if usuario:
            flash('El correo ya está registrado.', 'error')
            return redirect(url_for('registro'))
        
        # Crear usuario (inactivo)
        nuevo_usuario = Usuario(email=email, activo=False)
        nuevo_usuario.set_password(password)
        db.session.add(nuevo_usuario)
        db.session.commit()
        
        # Generar código de verificación
        codigo = nuevo_usuario.generar_codigo()
        
        # Enviar código por email
        if enviar_codigo_verificacion(email, codigo):
            # Guardamos el email en sesión para usarlo en el siguiente paso
            session['email_verificacion'] = email
            return redirect(url_for('verificar_codigo'))
        else:
            flash('Error al enviar el correo. Intenta más tarde.', 'error')
            db.session.delete(nuevo_usuario)
            db.session.commit()
            return redirect(url_for('registro'))
    
    # GET: mostrar formulario de registro
    return render_template('registro.html')

@app.route('/verificar_codigo', methods=['GET', 'POST'])
def verificar_codigo():
    if 'email_verificacion' not in session:
        return redirect(url_for('registro'))
    
    if request.method == 'POST':
        codigo = request.form['codigo']
        email = session['email_verificacion']
        usuario = Usuario.query.filter_by(email=email).first()
        
        if usuario and usuario.verificar_codigo(codigo):
            usuario.activo = True
            usuario.codigo_verificacion = None  # Limpiar código usado
            usuario.codigo_expira = None
            db.session.commit()
            session.pop('email_verificacion', None)
            flash('¡Correo verificado! Ahora puedes iniciar sesión.', 'success')
            return redirect(url_for('login'))
        else:
            flash('Código incorrecto o expirado.', 'error')
            return redirect(url_for('verificar_codigo'))
    
    # GET: mostrar formulario para ingresar código
    return render_template('verificar_codigo.html')  # Necesitas crear este HTML

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email'].strip().lower()
        password = request.form['password']
        
        usuario = Usuario.query.filter_by(email=email).first()
        if usuario and usuario.check_password(password):
            if not usuario.activo:
                flash('Debes verificar tu correo primero.', 'error')
                # Opcional: reenviar código
                return redirect(url_for('login'))
            # Inicio de sesión exitoso
            session['user_id'] = usuario.id
            session['user_email'] = usuario.email
            flash('Bienvenido', 'success')
            return redirect(url_for('cursos'))  # O a donde quieras
        else:
            flash('Credenciales incorrectas', 'error')
            return redirect(url_for('login'))
    
    return render_template('login.html')

@app.route('/cursos')
def cursos():
    if 'user_id' not in session:
        flash('Debes iniciar sesión', 'error')
        return redirect(url_for('login'))
    return render_template('cursos.html')

@app.route('/recuperar', methods=['GET', 'POST'])
def recuperar():
    if request.method == 'POST':
        email = request.form['email'].strip().lower()
        usuario = Usuario.query.filter_by(email=email).first()
        
        if usuario:
            # Generar y enviar código de recuperación
            codigo = usuario.generar_codigo()
            if enviar_codigo_recuperacion(email, codigo):
                session['email_recuperacion'] = email
                return redirect(url_for('verificar_recuperacion'))
            else:
                flash('Error al enviar correo', 'error')
        else:
            # No revelar si el correo existe o no por seguridad
            flash('Si el correo existe, recibirás un código', 'info')
        return redirect(url_for('recuperar'))
    
    return render_template('recuperar.html')  # Formulario para pedir email

@app.route('/verificar_recuperacion', methods=['GET', 'POST'])
def verificar_recuperacion():
    if 'email_recuperacion' not in session:
        return redirect(url_for('recuperar'))
    
    if request.method == 'POST':
        codigo = request.form['codigo']
        email = session['email_recuperacion']
        usuario = Usuario.query.filter_by(email=email).first()
        
        if usuario and usuario.verificar_codigo(codigo):
            # Código correcto, permitir cambiar contraseña
            session['puede_cambiar'] = True
            return redirect(url_for('cambiar_password'))
        else:
            flash('Código incorrecto o expirado', 'error')
            return redirect(url_for('verificar_recuperacion'))
    
    return render_template('verificar_codigo.html')  # Reutilizamos la misma plantilla

@app.route('/cambiar_password', methods=['GET', 'POST'])
def cambiar_password():
    if 'email_recuperacion' not in session or not session.get('puede_cambiar'):
        return redirect(url_for('recuperar'))
    
    if request.method == 'POST':
        password = request.form['password']
        confirm = request.form['confirm_password']
        
        if password != confirm:
            flash('Las contraseñas no coinciden', 'error')
            return redirect(url_for('cambiar_password'))
        
        email = session['email_recuperacion']
        usuario = Usuario.query.filter_by(email=email).first()
        if usuario:
            usuario.set_password(password)
            usuario.codigo_verificacion = None
            usuario.codigo_expira = None
            db.session.commit()
            # Limpiar sesión
            session.pop('email_recuperacion', None)
            session.pop('puede_cambiar', None)
            flash('Contraseña actualizada. Ahora inicia sesión.', 'success')
            return redirect(url_for('login'))
        else:
            flash('Error inesperado', 'error')
            return redirect(url_for('recuperar'))
    
    return render_template('cambiar_password.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Sesión cerrada', 'info')
    return redirect(url_for('index'))