# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Crear la aplicación Flask
app = Flask(__name__)

# Configuración de la aplicación
app.config['SECRET_KEY'] = 'contraseña_secreta_para_sesiones'  # Cambia esto por una clave segura
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:danieleduglobal123*@localhost/eduglobal'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la base de datos (se definirá en models.py)
db = SQLAlchemy(app)

# Importar las rutas (después de crear app para evitar importaciones circulares)
from routes import *

if __name__ == '__main__':
    app.run(debug=True)