from flask import Blueprint, request, jsonify
from app.Services.UsuarioService import UsuarioService

usuario_bp = Blueprint('usuario_bp', __name__)
usuario_service = UsuarioService()

@usuario_bp.route('/usuarios', methods=['GET'])
def obtener_todos_los_usuarios():
    usuarios = usuario_service.obtener_todos_los_usuarios()
    return jsonify([usuario.__dict__ for usuario in usuarios]), 200

@usuario_bp.route('/usuarios/<int:id>', methods=['GET'])
def obtener_usuario_por_id(id):
    usuario = usuario_service.obtener_usuario_por_id(id)
    if usuario:
        return jsonify(usuario.__dict__), 200
    return jsonify({'mensaje': 'Usuario no encontrado'}), 404

@usuario_bp.route('/usuarios', methods=['POST'])
def crear_usuario():
    datos = request.get_json()
    nombre = datos.get('nombre')
    nuevo_usuario = usuario_service.crear_usuario(nombre)
    response_data = {
        'id': nuevo_usuario.id,
        'nombre': nuevo_usuario.nombre
    }
    return jsonify(response_data), 201

@usuario_bp.route('/usuarios/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    usuario = usuario_service.obtener_usuario_por_id(id)
    if not usuario:
        return jsonify({'mensaje': 'Usuario no encontrado'}), 404
    usuario_service.actualizar_usuario()
    return jsonify(usuario.__dict__), 200

@usuario_bp.route('/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    usuario = usuario_service.obtener_usuario_por_id(id)
    if not usuario:
        return jsonify({'mensaje': 'Usuario no encontrado'}), 404
    usuario_service.eliminar_usuario(usuario)
    return jsonify({'mensaje': 'Usuario eliminado exitosamente'}), 200

