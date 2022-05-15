import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://mercy:mercy@localhost/pitch'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_TRACK_MODIFICATIONS = True



class ProdConfig(Config):
    '''Child
    '''
SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

DEBUG = True


class DevConfig(Config):
    ''' child class
    '''


config_options = {
'development':DevConfig,
'production':ProdConfig
}