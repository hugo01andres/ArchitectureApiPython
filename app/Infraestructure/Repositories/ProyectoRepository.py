from app.Infraestructure.Repositories.RepositoryBase import RepositorioBase
from app.Core.Models.Proyecto import Proyecto

class ProyectoRepository(RepositorioBase):
    def __init__(self):
        super().__init__(Proyecto)
