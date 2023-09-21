from pony.orm import Database, PrimaryKey, Required, Optional, Set
from models import User
from database import db

class Posts(db.Entity):
    id = PrimaryKey(int, auto=True)
    title = Required(str, 40)
    body = Required(str)
    user = Required("User")