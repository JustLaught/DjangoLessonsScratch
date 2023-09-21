from pony.orm import Database, PrimaryKey, Required, Optional, Set
from database import db
from models import Book
from models import Posts

class User(db.Entity):
    id_user = PrimaryKey(int, auto=True) #auto increment
    first_name = Required(str, 40)#required field
    last_name = Required(str, 40)
    age = Required(int)
    about = Optional(str)
    email = Required(str, unique=True)
    posts = Set("Posts")
    books = Set("Book")
    # books = Set("Books_Users")   # For class Book_Users

    def __str__ (self):
        return f"{self.first_name} {self.last_name} | {self.age} | {self.email}"