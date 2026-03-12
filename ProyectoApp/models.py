# models.py
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    activo = db.Column(db.Boolean, default=False)  # True cuando verifica email
    codigo_verificacion = db.Column(db.String(6), nullable=True)  # Código para email
    codigo_expira = db.Column(db.DateTime, nullable=True)  # Fecha de expiración del código

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generar_codigo(self):
        # Genera un código aleatorio de 6 dígitos
        import random
        self.codigo_verificacion = f"{random.randint(100000, 999999)}"
        # Expira en 10 minutos
        self.codigo_expira = datetime.datetime.utcnow() + datetime.timedelta(minutes=10)
        db.session.commit()
        return self.codigo_verificacion

    def verificar_codigo(self, codigo):
        if self.codigo_verificacion == codigo and self.codigo_expira > datetime.datetime.utcnow():
            return True
        return False

    def __repr__(self):
        return f'<Usuario {self.email}>'