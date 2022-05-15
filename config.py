import os

class Config:
    SECRET_KEY='Today'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mercy:mercy@localhost/pitch'
    UPLOADED_PHOTOS_DEST ='app/static/photos'



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