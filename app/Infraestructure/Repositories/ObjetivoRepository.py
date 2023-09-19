from app.Infraestructure.Repositories.RepositoryBase import RepositorioBase
from app.Core.Models.Objetivo import Objetivo

class ObjetivoRepository(RepositorioBase):
    def __init__(self):
        super().__init__(Objetivo)
