from app.Infraestructure.Repositories.UsuarioRepository import UsuarioRepository
from app.Core.Models.Usuario import Usuario

class UsuarioService:
    def __init__(self):
        self.usuario_repository = UsuarioRepository()

    def crear_usuario(self, nombre):
        nuevo_usuario = Usuario(nombre=nombre)
        self.usuario_repository.agregar(nuevo_usuario)
        print(nuevo_usuario)
        return nuevo_usuario

    def obtener_todos_los_usuarios(self):
        return self.usuario_repository.obtener_todos()

    def obtener_usuario_por_id(self, id):
        return self.usuario_repository.obtener_por_id(id)

    def actualizar_usuario(self, id, nuevo_nombre):
        usuario = self.usuario_repository.obtener_por_id(id)
        if usuario is not None:
            usuario.nombre = nuevo_nombre
            self.usuario_repository.actualizar(usuario)
            return usuario
        return None

    def eliminar_usuario(self, id):
        usuario = self.usuario_repository.obtener_por_id(id)
        if usuario is not None:
            self.usuario_repository.eliminar(usuario)
            return True
        return False

