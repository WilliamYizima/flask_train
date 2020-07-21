from flask import Flask
from flask_bootstrap import Bootstrap
from db.models import configure as config_db
from routes import usuario

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///teste.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JSON_AS_ASCII'] = False
    config_db(app)


    app.register_blueprint(usuario.user)
    return app


if __name__ == "__main__":
    create_app().run(debug=True)
