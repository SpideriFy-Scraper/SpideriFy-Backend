from datetime import timedelta
from common.db import redis_client
from urllib.parse import urlparse


def get_asin_from_cache(key: str) -> str:
    """Get data from redis."""

    val = redis_client.get(key)
    return val


def set_asin_to_cache(key: str, value: str) -> bool:
    """Set data to redis."""

    state = redis_client.setex(key, timedelta(seconds=3600), value=value, )
    return state


def get_asin_from_url(url: str) -> str:
    obj = urlparse(url)
    patha = obj.path
    if patha[-1] == "/":
        patha = patha[:-1]
    if patha[0] == "/":
        patha = patha[1:]
    return patha.split("/")[2]
