from flask import Blueprint, request, jsonify
from app.Services.ProyectoService import ProyectoService

proyecto_bp = Blueprint('proyecto_bp', __name__)
proyecto_service = ProyectoService()

@proyecto_bp.route('/proyectos', methods=['POST'])
def crear_proyecto():
    """Crea un proyecto.

    Crea un nuevo proyecto con el nombre proporcionado y una lista de objetivos.

    ---
    consumes:
      - application/json
    parameters:
      - name: proyecto
        in: body
        required: true
        description: Información del proyecto a crear.
        schema:
          type: object
          properties:
            nombre:
              type: string
              example: "Nombre del Proyecto"
            objetivos:
              type: array
              items:
                type: object
                properties:
                  titulo:
                    type: string
                    example: "Título del Objetivo"
                  descripcion:
                    type: string
                    example: "Descripción del Objetivo"
    responses:
      201:
        description: Proyecto creado exitosamente.
    """
    data = request.get_json()
    nombre = data.get('nombre')
    objetivos = data.get('objetivos', [])
    nuevo_proyecto = proyecto_service.crear_proyecto(nombre, objetivos)
    return 'Proyecto creado', 201

@proyecto_bp.route('/proyectos', methods=['GET'])
def obtener_todos_los_proyectos():
    """
    Obtiene todos los proyectos
    ---
    responses:
      200:
        description: Lista de proyectos
    """
    proyectos = proyecto_service.obtener_todos_los_proyectos()
    proyectos_dict = [{'id': proyecto.id, 'nombre': proyecto.nombre} for proyecto in proyectos]
    return jsonify(proyectos_dict), 200

@proyecto_bp.route('/proyectos/<int:id>', methods=['GET'])
def obtener_proyecto_por_id(id):
    """Obtiene un proyecto por su ID.

    Obtiene la información del proyecto con el ID proporcionado.

    ---
    parameters:
      - name: id
        in: path
        description: ID del proyecto a obtener.
        required: true
        type: integer
    responses:
      200:
        description: Información del proyecto.
      404:
        description: Proyecto no encontrado.
    """
    proyecto = proyecto_service.obtener_proyecto_por_id(id)
    if proyecto is not None:
        return jsonify({
            'id': proyecto.id,
            'nombre': proyecto.nombre
        }), 200
    return jsonify({'mensaje': 'Proyecto no encontrado'}), 404

@proyecto_bp.route('/proyectos/<int:id>', methods=['PUT'])
def actualizar_proyecto(id):
    """Actualiza un proyecto por su ID.

    Permite modificar la información de un proyecto existente.

    ---
    parameters:
      - name: id
        in: path
        description: ID del proyecto a actualizar.
        required: true
        type: integer
      - name: nombre
        in: body
        description: Nuevo nombre del proyecto.
        required: true
        schema:
          type: object
          properties:
            nombre:
              type: string
    responses:
      200:
        description: Proyecto actualizado correctamente.
      404:
        description: Proyecto no encontrado.
    """
    data = request.get_json()
    nombre = data.get('nombre')
    proyecto_actualizado = proyecto_service.actualizar_proyecto(id, nombre)
    if proyecto_actualizado is not None:
        return 'Proyecto Actualizado', 200
    return jsonify({'mensaje': 'Proyecto no encontrado'}), 404

@proyecto_bp.route('/proyectos/<int:id>', methods=['DELETE'])
def eliminar_proyecto(id):
    """Elimina un proyecto.

    Elimina el proyecto con el ID proporcionado.

    ---
    parameters:
      - name: id
        in: path
        description: ID del proyecto a eliminar.
        required: true
        type: integer
    responses:
      200:
        description: Proyecto eliminado correctamente.
      404:
        description: Proyecto no encontrado.
    """
    eliminado = proyecto_service.eliminar_proyecto(id)
    if eliminado:
        return jsonify({'mensaje': 'Proyecto eliminado correctamente'}), 200
    return jsonify({'mensaje': 'Proyecto no encontrado'}), 404
