from peewee import *
from playhouse.postgres_ext import *

from fannypack.enum import Enum

from datetime import datetime

import uuid, redis

redis = redis.Redis()

db_conn = PostgresqlExtDatabase("club",
    user="club",
    password="club",
    threadlocals=True,
    port=5432)

from models import db
db.initialize(db_conn)


"""
models = [
    User,
    UserBan,
    Server,
    Game,
    GameTeam,
    GamePlayer
]
"""
