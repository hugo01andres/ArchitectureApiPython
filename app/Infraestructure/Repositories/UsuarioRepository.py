from app.Core.Models.Usuario import Usuario
from app.Infraestructure.Repositories.RepositoryBase import RepositorioBase

class UsuarioRepository(RepositorioBase):
    def __init__(self):
        super().__init__(Usuario)

