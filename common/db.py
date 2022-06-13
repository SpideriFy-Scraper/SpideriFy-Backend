from flask_sqlalchemy import SQLAlchemy
from config import Config
import redis
import sys


def redis_connect() -> redis.client.Redis:
    try:
        client = redis.Redis(
            host=Config.REDIS_HOST,
            port=Config.REDIS_PORT,
            password=Config.REDIS_PASS,
            db=0,
            socket_timeout=5,
        )
        ping = client.ping()
        if ping is True:
            return client
    except redis.AuthenticationError:
        print("AuthenticationError")
        sys.exit(1)


db = SQLAlchemy()
redis_client = redis_connect()
