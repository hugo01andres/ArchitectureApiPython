from flask import Blueprint, request, jsonify
from app.Services.UsuarioService import UsuarioService

usuario_bp = Blueprint('usuario_bp', __name__)
usuario_service = UsuarioService()

@usuario_bp.route('/usuarios', methods=['POST'])
def crear_usuario():
    """Crea un usuario.

    Crea un nuevo usuario con el nombre proporcionado.

    ---
    consumes:
      - application/json
    parameters:
      - name: nombre
        in: body
        required: true
        description: Nombre del usuario a crear.
        schema:
          type: object
          properties:
            nombre:
              type: string
              example: ""
    responses:
      201:
        description: Usuario creado exitosamente.
    """
    print(request.get_json())
    data = request.get_json()
    nombre = data.get('nombre')
    nuevo_usuario = usuario_service.crear_usuario(nombre)
    return 'Usuario creado',201

@usuario_bp.route('/usuarios', methods=['GET'])
def obtener_todos_los_usuarios():
    """
    Obtiene todos los usuarios
    ---
    responses:
      200:
        description: Lista de usuarios
    """
    usuarios = usuario_service.obtener_todos_los_usuarios()
    usuarios_dict = [{'id': usuario.id, 'nombre': usuario.nombre} for usuario in usuarios]
    return jsonify(usuarios_dict), 200

@usuario_bp.route('/usuarios/<int:id>', methods=['GET'])
def obtener_usuario_por_id(id):
    usuario = usuario_service.obtener_usuario_por_id(id)
    if usuario is not None:
        return jsonify(usuario.__dict__), 200
    return jsonify({'mensaje': 'Usuario no encontrado'}), 404

@usuario_bp.route('/usuarios/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    data = request.get_json()
    nombre = data.get('nombre')
    usuario_actualizado = usuario_service.actualizar_usuario(id, nombre)
    if usuario_actualizado is not None:
        return jsonify(usuario_actualizado.__dict__), 200
    return jsonify({'mensaje': 'Usuario no encontrado'}), 404

@usuario_bp.route('/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    eliminado = usuario_service.eliminar_usuario(id)
    if eliminado:
        return jsonify({'mensaje': 'Usuario eliminado correctamente'}), 200
    return jsonify({'mensaje': 'Usuario no encontrado'}), 404

