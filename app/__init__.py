from flask import Flask
from flask_bootstrap import Bootstrap
from .config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
photos = UploadSet('photos',IMAGES)

login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):

    app = Flask(__name__)
    # app.config["SQLALCHEMY_DATABASE_URI"] = ("postgresql://mercy:mercy@localhost/pitch")
    # app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
   

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    configure_uploads(app,photos)

    #.......

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    # Will add the views and forms

    return app