from utils.db_api import db
from peewee import *
from datetime import datetime


class User(Model):
    id = BigIntegerField(primary_key=True, null=False, index=True, unique=True)
    username = CharField(max_length=32, null=True)
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        database = db
