from pony.orm import Database, PrimaryKey, Required, Optional, Set
from database import db
from models import User

class Book(db.Entity):
    name = Required(str, 60)
    author = Required(str, 40)
    users = Set("User")
    # users = Set("Books_Users")  # For class Books_Users


# # class Books_Users(db.Entity):
# #     id = PrimaryKey(int, auto=True)
# #     user = Optional("User")
# #     book = Optional("Book")