# email_utils.py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuración del servidor SMTP (ejemplo con Gmail)
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USER = 'tu_correo@gmail.com'      # Cambiar por tu correo
SMTP_PASSWORD = 'tu_contraseña_app'    # Usa una contraseña de aplicación

def enviar_correo(destinatario, asunto, cuerpo):
    """Envía un correo HTML al destinatario."""
    msg = MIMEMultipart()
    msg['From'] = SMTP_USER
    msg['To'] = destinatario
    msg['Subject'] = asunto

    msg.attach(MIMEText(cuerpo, 'html'))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        print(f"Error al enviar correo: {e}")
        return False

def enviar_codigo_verificacion(email, codigo):
    """Envía el código de verificación al correo del usuario."""
    asunto = "Código de verificación - EduGlobal"
    cuerpo = f"""
    <h2>Verificación de correo</h2>
    <p>Tu código de verificación es: <strong>{codigo}</strong></p>
    <p>Este código expirará en 10 minutos.</p>
    """
    return enviar_correo(email, asunto, cuerpo)

def enviar_codigo_recuperacion(email, codigo):
    """Envía el código para recuperar contraseña."""
    asunto = "Recuperación de contraseña - EduGlobal"
    cuerpo = f"""
    <h2>Recupera tu contraseña</h2>
    <p>Has solicitado restablecer tu contraseña.</p>
    <p>Tu código de verificación es: <strong>{codigo}</strong></p>
    <p>Este código expirará en 10 minutos.</p>
    """
    return enviar_correo(email, asunto, cuerpo)