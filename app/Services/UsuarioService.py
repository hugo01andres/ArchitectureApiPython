from app.Infraestructure.Repositories.UsuarioRepository import UsuarioRepository

class UsuarioService:
    def __init__(self):
        self.usuario_repo = UsuarioRepository()

    def crear_usuario(self, nombre):
        return self.usuario_repo.crear_usuario(nombre)

    def obtener_usuario_por_id(self, id):
        return self.usuario_repo.obtener_por_id(id)

    def obtener_todos_los_usuarios(self):
        return self.usuario_repo.obtener_todos()

    def actualizar_usuario(self):
        self.usuario_repo.actualizar()

    def eliminar_usuario(self, usuario):
        self.usuario_repo.eliminar(usuario)

