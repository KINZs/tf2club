from . import BModel
from .user import User

from datetime import datetime

from peewee import *

class UserBan(BModel):
    user = ForeignKeyField(User, related_name="bans")
    mod = ForeignKeyField(User, related_name="banned_players")
    reason = CharField()

    created = DateTimeField(default=datetime.utcnow)
    expires = DateTimeField(null=True)
