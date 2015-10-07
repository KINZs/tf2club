import json

from . import BModel

from peewee import *
from fannypack.enum import Enum

from datetime import datetime

Group = Enum("normal", "moderator", "admin", "super")

class User(BModel):
    class Meta:
        db_table = "users"

    steamid = CharField(max_length=128, unique=True)
    nickname = CharField(default='')
    email = CharField(max_length=254, unique=True, null=True)

    created_at = DateTimeField(default=datetime.utcnow)
    last_login = DateTimeField(default=datetime.utcnow)

    group = IntegerField(default=Group.NORMAL)

    def get_steam_profile(self):
        from app import fanny, steam
        profile = fanny.redis.get('user:{}:profile'.format(self.steamid))

        if profile:
            return json.loads(profile)

        profile = steam.get_user_info(self.steamid)

        if 'profileurl' in profile:
            profile['vanityname'] = profile['profileurl'].rsplit('/', 2)[1]

        fanny.redis.setex('user:{}:profile'.format(self.steamid), json.dumps(profile), 60 * 30)
        return profile

    def to_dict(self, perspective=None):
        base = {
            'id': self.id,
            'steamid': self.steamid,
            'nickname': self.nickname
        }

        if perspective.group >= Group.MODERATOR:
            base['created_at'] = self.created_at
            base['last_login'] = self.last_login
            base['group'] = str(Group[self.group])

        if perspective.group >= Group.SUPER:
            base['email'] = self.email

        return base
