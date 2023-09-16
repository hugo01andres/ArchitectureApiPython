from app.app import create_app
from app.Infraestructure.db import db

# Crea una instancia de la aplicación Flask
app = create_app()

# Inicializa la base de datos
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
