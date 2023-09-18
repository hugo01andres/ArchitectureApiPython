from app.Infraestructure.Repositories.UsuarioRepository import UsuarioRepository

class UsuarioService:
    def __init__(self):
        self.usuario_repository = UsuarioRepository()

    def crear_usuario(self, nombre):
        nuevo_usuario = self.usuario_repository.agregar(nombre=nombre)
        return nuevo_usuario

    def obtener_todos_los_usuarios(self):
        return self.usuario_repository.obtener_todos()

    def obtener_usuario_por_id(self, id):
        return self.usuario_repository.obtener_por_id(id)

    def actualizar_usuario(self, id, nombre):
        usuario = self.usuario_repository.obtener_por_id(id)
        if usuario is not None:
            usuario.nombre = nombre
            self.usuario_repository.actualizar(usuario)
            return usuario
        return None

    def eliminar_usuario(self, id):
        usuario = self.usuario_repository.obtener_por_id(id)
        if usuario is not None:
            self.usuario_repository.eliminar(usuario)
            return True
        return False

