import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    Debug = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'eita'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
