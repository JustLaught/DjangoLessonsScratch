from pony.orm import Database, PrimaryKey, Required, Optional, Set

db = Database()
db.bind(provider="postgres", user="postgres", password="2773", host="localhost", database="Pony")