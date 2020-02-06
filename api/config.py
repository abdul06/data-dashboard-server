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
    SQLALCHEMY_DATABASE_URI='postgresql://' + db_user + ':' + user_password + '@' + db_host + ':' + db_port + '/' + db_name
        
