from app.Infraestructure.Repositories.ProyectoRepository import ProyectoRepository
from app.Infraestructure.Repositories.ObjetivoRepository import ObjetivoRepository
from app.Core.Models.Proyecto import Proyecto
from app.Core.Models.Objetivo import Objetivo

class ProyectoService:
    def __init__(self):
        self.proyecto_repository = ProyectoRepository()
        self.objetivo_repository = ObjetivoRepository()

    def crear_proyecto(self, nombre, objetivos):
        nuevo_proyecto = Proyecto(nombre=nombre)
        self.proyecto_repository.agregar(nuevo_proyecto)

        for objetivo_data in objetivos:
            nuevo_objetivo = Objetivo(titulo=objetivo_data['titulo'], descripcion=objetivo_data['descripcion'], proyecto=nuevo_proyecto)
            self.objetivo_repository.agregar(nuevo_objetivo)

        return nuevo_proyecto

    def obtener_todos_los_proyectos(self):
        return self.proyecto_repository.obtener_todos()

    def obtener_proyecto_por_id(self, id):
        return self.proyecto_repository.obtener_por_id(id)

    def actualizar_proyecto(self, id, nuevo_nombre):
        proyecto = self.proyecto_repository.obtener_por_id(id)
        if proyecto is not None:
            proyecto.nombre = nuevo_nombre
            self.proyecto_repository.actualizar(proyecto)
            return proyecto
        return None

    def eliminar_proyecto(self, id):
        proyecto = self.proyecto_repository.obtener_por_id(id)
        if proyecto is not None:
            self.proyecto_repository.eliminar(proyecto)
            return True
        return False
    
    def obtener_proyectos_con_objetivos(self):
        proyectos = self.proyecto_repository.obtener_todos()
        proyectos_con_objetivos = []

        for proyecto in proyectos:
            objetivos = self.proyecto_repository.obtener_por_proyecto_id(proyecto.id)
            proyectos_con_objetivos.append({
                'id': proyecto.id,
                'nombre': proyecto.nombre,
                'objetivos': [{'id': objetivo.id, 'titulo': objetivo.titulo, 'descripcion': objetivo.descripcion} for objetivo in objetivos]
            })

        return proyectos_con_objetivos


    def agregar_objetivo_a_proyecto(self, proyecto_id, titulo, descripcion):
        proyecto = self.proyecto_repository.obtener_por_id(proyecto_id)

        if proyecto is not None:
            nuevo_objetivo = Objetivo(titulo=titulo, descripcion=descripcion, proyecto=proyecto)
            self.objetivo_repository.agregar(nuevo_objetivo)
            return nuevo_objetivo

        return None
