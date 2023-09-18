from app.Infraestructure.db import db

class RepositorioBase:
    def __init__(self, model):
        self.model = model
        self.db = db

    def agregar(self, entidad):
        try:
            self.db.session.add(entidad)
            self.db.session.commit()
        except Exception as e:
            self.db.session.rollback()
            raise e

    def obtener_por_id(self, id):
        return self.model.query.get(id)

    def obtener_todos(self):
        return self.model.query.all()

    def actualizar(self):
        try:
            self.db.session.commit()
        except Exception as e:
            self.db.session.rollback()
            raise e

    def eliminar(self, entidad):
        try:
            self.db.session.delete(entidad)
            self.db.session.commit()
        except Exception as e:
            self.db.session.rollback()
            raise e

