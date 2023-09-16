from app.Core.Models.Usuario import Usuario
from app.Infraestructure.Repositories.RepositoryBase import RepositorioBase

class UsuarioRepository(RepositorioBase):
    def __init__(self):
        super().__init__()
        self.modelo = Usuario

    def crear_usuario(self, nombre):
        nuevo_usuario = self.modelo(nombre=nombre)
        self.agregar(nuevo_usuario)
        return nuevo_usuario

