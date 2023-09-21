from pony.orm import Database

db = Database()
db.bind(provider="postgres", user="postgres", host="localhost", password="2773", database="Academy")