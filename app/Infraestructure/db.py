from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from pathlib import Path


load_dotenv('../../.env')
print("Variables de entorno cargadas con éxito.")
print(os.getenv('DATABASE_URL'))


db = SQLAlchemy()

def init_app(app):
    print(os.getenv('DATABASE_URL'))
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

