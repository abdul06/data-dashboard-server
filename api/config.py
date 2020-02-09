"""
Config Class Setup up database connection and reteive environment varialbes.
"""
import os

class Config:
    # Class Variables
    db_name = os.environ.get("DB_NAME")
    db_host = os.environ.get("DB_HOST")
    db_port = os.environ.get("DB_PORT")
    db_user = os.environ.get("DB_USER")
    user_password = os.environ.get("DB_PASSWORD")
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class DevelopmentConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = Config.SQLALCHEMY_TRACK_MODIFICATIONS
    SQLALCHEMY_DATABASE_URI='postgresql://{user}:{password}@{host}:{port}/{db_name}'.format(user=Config.db_user,password=Config.user_password,host=Config.db_host,port=Config.db_port,db_name=Config.db_name)

class ProductionConfig(Config):
    instance_name = os.environ.get("INSTANCE_NAME")

    SQLALCHEMY_TRACK_MODIFICATIONS = Config.SQLALCHEMY_TRACK_MODIFICATIONS
    # pg8000, unix_sock
    SQLALCHEMY_DATABASE_URI = 'postgres+pg8000://{user}:{password}@/{db_name}?unix_sock=/cloudsql/{instance_name}/.s.PGSQL.5432'.format(user=Config.db_user,password=Config.user_password,db_name=Config.db_name, instance_name=instance_name,port=Config.db_port)

    

config_env = dict(
    dev=DevelopmentConfig,
    prod=ProductionConfig
)