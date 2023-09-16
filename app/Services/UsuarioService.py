from app.Infraestructure.Repositories.UsuarioRepository import UsuarioRepository

class UsuarioService:
    def __init__(self, db):
        self.usuario_repo = UsuarioRepository(db)

    def crear_usuario(self, id, nombre):
        nuevo_usuario = self.usuario_repo.modelo(id=id, nombre=nombre)
        self.usuario_repo.agregar(nuevo_usuario)
        return nuevo_usuario

    def obtener_usuario_por_id(self, id):
        return self.usuario_repo.obtener_por_id(id)

    def obtener_todos_los_usuarios(self):
        return self.usuario_repo.obtener_todos()

    def actualizar_usuario(self):
        self.usuario_repo.actualizar()

    def eliminar_usuario(self, usuario):
        self.usuario_repo.eliminar(usuario)
