from flask import Blueprint, request, jsonify
from app.Services.UsuarioService import UsuarioService
from app.Infraestructure.db import db

usuario_bp = Blueprint('usuario_bp', __name__)
usuario_service = UsuarioService(db)  # Asegúrate de tener acceso a la instancia de la base de datos (db).

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
    id = datos.get('id')
    nombre = datos.get('nombre')
    nuevo_usuario = usuario_service.crear_usuario(id, nombre)
    return jsonify(nuevo_usuario.__dict__), 201

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
