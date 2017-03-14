import os
from enum import Enum
from tornado.ioloop import IOLoop


if os.getenv('MYSQL_HOST'):
    mysql_host = os.getenv('MYSQL_HOST')
else:
    mysql_host = '127.0.0.1'

if os.getenv('MYSQL_PORT'):
    mysql_port = os.getenv('MYSQL_PORT')
else:
    mysql_port = '3306'

if os.getenv('REDIS_HOST'):
    redis_host = os.getenv('REDIS_HOST')
else:
    redis_host = '127.0.0.1'

if os.getenv('REDIS_PORT'):
    redis_port = os.getenv('REDIS_PORT')
else:
    redis_port = '6379'

class Config(Enum):
    MYSQL_HOST = mysql_host
    MYSQL_PORT = mysql_port
    REDIS_HOST = redis_host
    REDIS_PORT = redis_port

BABBLE_LOOP = IOLoop.configure('tornado.platform.asyncio.AsyncIOLoop')
