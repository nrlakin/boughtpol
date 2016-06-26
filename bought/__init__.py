import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from flask_mail import Mail
from config import config

db = SQLAlchemy()
moment = Moment()
mail = Mail()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    moment.init_app(app)
    mail.init_app(app)

    from bought.frontend import frontend as frontend_module
    from bought.getter import getter as getter_module

    app.register_blueprint(frontend_module, url_prefix=None)
    app.register_blueprint(getter_module, url_prefix='/getter')

    return app
