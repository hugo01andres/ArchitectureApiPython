from app.Infraestructure.db import db

class Proyecto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    objetivos = db.relationship('Objetivo', backref='proyecto', lazy=True)

