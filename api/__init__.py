from flask import Flask
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow 
from api.config import Config

db = SQLAlchemy()
ma = Marshmallow()

def create_app(config_class=Config):
    """ create intance of rest api

    Attributes:
        app: init of Flask application
        db: SQLAlchemy for speaking to the database orm
        ma: Marshmallow init for serializing database data

    :param {Object} Config: Take config object to be passed to from_object() method on app.config
        exp: { SQLALCHEMY_TRACK_MODIFICATIONS: bool, SQLALCHEMY_DATABASE_URI: url_to_database }

    :return: {Object} app: application object to run project
    """
    # setup app config
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)
    
    # initialize db
    db.init_app(app)
    # Init ma
    ma.init_app(app)

    # any modules that need access to app put in with [app].app_context():
    # allows perform database operations outside an application context,
    with app.app_context():
        from api import routes # imports need to be after  app creation
    
    return app
