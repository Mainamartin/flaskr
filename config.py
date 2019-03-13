import os
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = os.urandom(30)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///posts.db'


class DevelopmentConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False