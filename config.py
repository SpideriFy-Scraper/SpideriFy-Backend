from dotenv import dotenv_values
config = dotenv_values(".env")

class Config(object):
    """Base config, uses staging Database Server."""
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = config["SECRET_KEY"]
    # Config Database
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{config["DB_USER"]}:{config["DB_PASSWORD"]}@localhost:3306/spiderify'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    DEVELOPMENT = True
    TESTING = True
    PROPAGATE_EXCEPTIONS = True

