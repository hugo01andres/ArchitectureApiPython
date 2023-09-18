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
    """Obtiene un usuario por su ID.

    Obtiene la información del usuario con el ID proporcionado.

    ---
    parameters:
      - name: id
        in: path
        description: ID del usuario a obtener.
        required: true
        type: integer
    responses:
      200:
        description: Información del usuario.
      404:
        description: Usuario no encontrado.
    """
    usuario = usuario_service.obtener_usuario_por_id(id)
    if usuario is not None:
        return jsonify({
            'id': usuario.id,
            'nombre': usuario.nombre
        }), 200
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
    """Elimina un usuario.

    Elimina el usuario con el ID proporcionado.

    ---
    parameters:
      - name: id
        in: path
        description: ID del usuario a eliminar.
        required: true
        type: integer
    responses:
      200:
        description: Usuario eliminado correctamente.
      404:
        description: Usuario no encontrado.
    """
    eliminado = usuario_service.eliminar_usuario(id)
    if eliminado:
        return jsonify({'mensaje': 'Usuario eliminado correctamente'}), 200
    return jsonify({'mensaje': 'Usuario no encontrado'}), 404

