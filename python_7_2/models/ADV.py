from database import db
from pony.orm import PrimaryKey, Optional, Required

class Adv(db.Entity):
    id = PrimaryKey(int, auto=True, column="ID")
    name = Required(str, 30, column="Name")
    year = Required(int, column="Year")
    dp_id = Optional(int, column="DepartmentID")
    rating = Required(int, column="Rating")

    def __str__ (self):
        return f"[{self.id}] | Name: {self.name} | Year: {self.year} | Rating: {self.rating}"