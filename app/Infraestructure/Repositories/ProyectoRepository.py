from app.Infraestructure.Repositories.RepositoryBase import RepositorioBase
from app.Core.Models.Proyecto import Proyecto
from app.Core.Models.Objetivo import Objetivo

class ProyectoRepository(RepositorioBase):
    def __init__(self):
        super().__init__(Proyecto)

    def obtener_por_proyecto_id(self, proyecto_id):
        return self.db.session.query(Objetivo).filter(Objetivo.proyecto_id == proyecto_id).all()

