from app.app import create_app
from app.Infraestructure.db import db
from flask import redirect

# Crea una instancia de la aplicación Flask
app = create_app()


# Inicializa la base de datos
with app.app_context():
    db.create_all()

@app.route('/')
def redirect_to_swagger():
    return redirect('/apidocs')

if __name__ == '__main__':
    app.run(debug=True)
