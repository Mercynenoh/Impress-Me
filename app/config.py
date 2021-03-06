import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://mercy:mercy@localhost/pitch'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass



class ProdConfig(Config):
    '''Child
    '''
SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://mercy:mercy@localhost/pitch'

DEBUG =True
    
    
    

class DevConfig(Config):
    ''' child class
    '''
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://mercy:mercy@localhost/pitch'
    

config_options = {
'development':DevConfig,
'production':ProdConfig
}