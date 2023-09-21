from faker import Faker
import random
from database import Database as DB
from json import *
faker = Faker()


class Shoes:
    def __init__(self, sex: str, type: str, color: str, price: int, country: str, size: int):
        self.sex = sex
        self.type = type
        self.color = color
        self.price = price
        self.country = country
        self.size = size
        

    def __str__(self):
        return f"{self.sex} | {self.type} | {self.color} | {self.size} | {self.country}"
    
    @classmethod
    def get_all_films(cls):
        data = DB.shoes
        return data

    @classmethod
    def create_fake_shoes(cls):     
        for _ in range(6):
            obj = {
            "sex": random.choice(["Male", "Female"]),
            "type": random.choice(["Sneakers", "Boots", "Loafers"]),
            "color": random.choice(["Black", "White", "Red", "Blue", "Green", "Yellow", "Brown"]),
            "price": random.randint(200, 500),
            "country": random.choice(["USA", "China", "Japan", "Germany", "France", "Italy"]),
            "size": random.randint(14, 17)
            }
            DB.shoes.append(obj)

    @staticmethod
    def save_db_in_file():
        with open("database.txt", 'w') as f:
            data = DB.shoes
            if data:
                dump(data, f)

    @staticmethod
    def load_db_from_file():
        try:
            with open("database.txt", 'r') as f:
                data = load(f)
                print(data)
                if data:
                    DB.shoes.append(data)
        except:
            pass
            