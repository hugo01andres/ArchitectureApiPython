class RepositorioBase:
    def __init__(self, db):
        self.db = db

    def agregar(self, entidad):
        self.db.session.add(entidad)
        self.db.session.commit()

    def obtener_por_id(self, id):
        return self.modelo.query.get(id)

    def obtener_todos(self):
        return self.modelo.query.all()

    def actualizar(self):
        self.db.session.commit()

    def eliminar(self, entidad):
        self.db.session.delete(entidad)
        self.db.session.commit()
