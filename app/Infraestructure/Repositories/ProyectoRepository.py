from app.Infraestructure.Repositories.RepositoryBase import RepositorioBase
from app.Core.Models.Proyecto import Proyecto
from app.Core.Models.Objetivo import Objetivo

class ProyectoRepository(RepositorioBase):
    def __init__(self):
        super().__init__(Proyecto)

    def obtener_proyectos_con_objetivos(self):
        return self.db.session.query(Proyecto, Objetivo).join(Proyecto.objetivos).all()

