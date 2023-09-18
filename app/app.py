from flask import Flask
from app.Infraestructure.db import db
from app.Presentation.UsuarioController import usuario_bp
from dotenv import load_dotenv
import os

load_dotenv()


def create_app():
    app = Flask(__name__)
    print(os.getenv('DATABASE_URL'))
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    # Registra los blueprints
    app.register_blueprint(usuario_bp)

    return app
