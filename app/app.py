from flask import Flask
from app.Infraestructure.db import db
from app.Presentation.UsuarioController import usuario_bp
from dotenv import load_dotenv
def create_app():
    app = Flask(__name__)
    db.init_app(app)

    # Registra los blueprints
    app.register_blueprint(usuario_bp)

    return app
