from dotenv import dotenv_values

config = dotenv_values(".spiderify.env")


class Config(object):
    """Base config, uses staging Database Server."""

    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = config["SECRET_KEY"]
    JWT_SECRET_KEY = config["JWT_SECRET_KEY"]
    # Config Database
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{config["DB_USER"]}:{config["DB_PASSWORD"]}@localhost:3306/{config["DB_NAME"]}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = True
    SENTIMENT_URI = config["SENTIMENT_URI"]
    SUMMARIZATION_URI = config["SUMMARIZATION_URI"]
    REDIS_HOST = config["REDIS_HOST"]
    REDIS_PASS = config["REDIS_PASS"]
    REDIS_PORT = config["REDIS_PORT"]


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{config["DB_USER"]}:{config["DB_PASSWORD"]}@{config["PROXYSQL_HOSTNAME"]}:{config["PROXYSQL_PORT"]}/{config["DB_NAME"]}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    DEVELOPMENT = True
    TESTING = True
