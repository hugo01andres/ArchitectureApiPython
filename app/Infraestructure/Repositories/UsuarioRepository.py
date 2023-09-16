from RepositoryBase import RepositorioBase
from app.Core.Models.Usuario import Usuario

class UsuarioRepository(RepositorioBase):
    def __init__(self, db):
        super().__init__(db)
        self.modelo = Usuario
