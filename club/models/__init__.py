
from peewee import *

db = Proxy()

class BModel(Model):
    class Meta:
        database = db
