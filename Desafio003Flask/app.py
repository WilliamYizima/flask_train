from flask import Flask, request, jsonify, render_template, url_for
from db.models import configure as config_db
from flask_login import LoginManager
import os

login_manager = LoginManager()
login_manager.login_view = 'auth.login'


def create_app():
    app = Flask(__name__)

    # login_manager = LoginManager()
    # login_manager.login_view = url_for(login)
    app.config['JSON_AS_ASCII'] = False
    app.config.from_object(os.environ['APP_SETTINGS'])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    login_manager.init_app(app)


    config_db(app)
    db = app.db

    from routes.main import main as main_blueprint
    from routes.auth import auth as auth_blueprint
    from routes.post import post as post_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(post_blueprint, url_prefix='/post')
    from db.models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    # TODO fazer blueprint com __init__


    return app


if __name__ == '__main__':
    create_app().run()
