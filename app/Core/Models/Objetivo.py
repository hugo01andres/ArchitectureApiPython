from app.Infraestructure.db import db

class Objetivo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    proyecto_id = db.Column(db.Integer, db.ForeignKey('proyecto.id'), nullable=False)
