# Proyecto API Flask

Este proyecto es una API construida con Flask, una popular biblioteca de Python para crear aplicaciones web. La API gestiona usuarios y proporciona funcionalidades básicas como crear, leer, actualizar y eliminar (CRUD) usuarios.

## Configuración del Entorno

### Requisitos

- Python 3.x
- Flask
- Flask SQLAlchemy
- PostgreSQL

### Pasos para Configurar el Proyecto

1. Clona el repositorio desde GitHub:

```bash
git clone https://github.com/tu-usuario/tu-repositorio.git

pip install -r requirements.txt

python main.py
```
# Estructura del Proyecto
- app/
- Presentation/: Controladores de la API.
- Service/: Lógica de negocio y servicios.
- Repository/: Operaciones de base de datos.
- Model/: Definición de modelos de datos.
- Infraestructure/: Configuraciones de la aplicación.
- main.py: Punto de entrada de la aplicación.
- .env: Archivo de configuración de variables de entorno.
- requirements.txt: Lista de dependencias del proyecto.
# Uso de la API
# # La API proporciona las siguientes rutas:

- GET /usuarios: Obtiene todos los usuarios.
- GET /usuarios/{id}: Obtiene un usuario por su ID.
- POST /usuarios: Crea un nuevo usuario.
- PUT /usuarios/{id}: Actualiza un usuario existente.
- DELETE /usuarios/{id}: Elimina un usuario.
Para más detalles, consulta la documentación de la API.