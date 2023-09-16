from flask import Flask
from app.Infraestructure.db import db
from app.Presentation.UsuarioController import usuario_bp

def create_app():
    app = Flask(__name__)

    # Configura la base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    db.init_app(app)

    # Registra los blueprints
    app.register_blueprint(usuario_bp)

    return app
