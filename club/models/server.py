from . import BModel
from .user import User

from peewee import *

class Server(BModel):
    host = CharField(unique=True)
    game_port = IntegerField()
    rcon_port = IntegerField()
    rcon_pw = CharField()
