from flask import Flask
from config import config_options
from .main import main as main_blueprint
from .requests import configure_request


def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(config_options[config_name])
    app.register_blueprint(main_blueprint)
    configure_request(app)
    return app


from app.main import views



