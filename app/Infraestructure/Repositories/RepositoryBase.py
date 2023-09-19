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

    def actualizar(self,entidad):
        try:
            self.db.session.merge(entidad)
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
    
    def obtener_por_filtro(self, filtros):
        try:
            query = self.db.session.query(self.model)

            for campo, valor in filtros.items():
                query = query.filter(getattr(self.model, campo) == valor)
            return query.all()

        except Exception as e:
            self.db.session.rollback()
            raise e

    def obtener_todos_ordenados(self, atributo):
        return self.model.query.order_by(getattr(self.model, atributo)).all()
    
    def obtener_por_pagina(self, pagina, elementos_por_pagina):
        return self.model.query.paginate(pagina, elementos_por_pagina, False).items
    
    def contar_entidades(self):
        return self.model.query.count()
    
    def filtrar_por_rango(self, atributo, valor_minimo, valor_maximo):
        return self.model.query.filter(getattr(self.model, atributo).between(valor_minimo, valor_maximo)).all()
    
    def consulta_personalizada(self, *args, **kwargs):
        return self.model.query.filter(*args, **kwargs).all()
    
    def iniciar_transaccion(self):
        self.db.session.begin_nested()

    def confirmar_transaccion(self):
        self.db.session.commit()

    def revertir_transaccion(self):
        self.db.session.rollback()







