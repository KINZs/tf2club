from . import BModel
from .server import Server

from peewee import *
from fannypack.enum import Enum

GameState = Enum("new", "picking", "started", "ended", "closed")

class Game(BModel):
    server = ForeignKeyField(Server)
    mapp = CharField()
    
    state = IntegerField(default=GameState.NEW)
