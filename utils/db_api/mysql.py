import playhouse.shortcuts
from peewee import *
from data.config import *
from os import getenv
from dotenv import load_dotenv

load_dotenv()

database = getenv('mysqlDatabase')
user = getenv('mysqlUser')
password = getenv('mysqlPassword')


class ReconnectMySQLDatabase(playhouse.shortcuts.ReconnectMixin, MySQLDatabase):
    pass


db = ReconnectMySQLDatabase(database, user=user, password=password)
db.connect()
