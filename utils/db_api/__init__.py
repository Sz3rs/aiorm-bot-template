from dotenv import load_dotenv

load_dotenv()

if getenv('DBtype') == 'mysql':
  from .mysql import db
else:
  from .sqlite import db
