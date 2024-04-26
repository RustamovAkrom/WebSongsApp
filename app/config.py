import os

from dotenv import load_dotenv
load_dotenv()


class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, 'sqlite.db')
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config_mapping = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}
