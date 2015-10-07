from . import BModel
from .game import Game

from peewee import *

class GameTeam(BModel):
    game = ForeignKeyField(Game)
    score = IntegerField(default=0)

