from dotenv import load_dotenv
from os import getenv

load_dotenv()

if getenv('DBtype') == 'mysql':
  from .mysql import db
else:
  from .sqlite import db
