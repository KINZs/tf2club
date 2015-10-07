from . import BModel

from .game import Game
from .user import User
from .gameteam import GameTeam

from peewee import *
from fannypack.enum import Enum

Class = Enum("scout", "roamer", "pocket", "demo", "medic")

class GamePlayer(BModel):
    game = ForeignKeyField(Game)
    user = ForeignKeyField(User)
    team = ForeignKeyField(GameTeam)

    # Class this player is picked for
    cls = IntegerField(null=True)

    ringer = BooleanField(default=False)
    removed = BooleanField(default=False)
