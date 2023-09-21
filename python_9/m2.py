from faker import Faker
import random
from database import Database as DB
faker = Faker()


class Film:
    def __init__(self, name, genre, director, year, lenght, studio, actors :dict):
        self.name = name
        self.genre = genre
        self.director = director
        self.year = year
        self.length = lenght
        self.studio = studio
        self.actors = actors

    def __str__(self):
        return f"{self.name} | {self.genre} | {self.director} | {self.actors}"
    
    @classmethod
    def get_all_films(cls):
        data = DB.movie
        return data

    @classmethod
    def create_fake_films(cls):
        for _ in range(10):
            actors =[]
            for _ in range(6):
                actors.append({"first_name": faker.first_name(), "last_name": faker.last_name()})
            obj = {
                "name": faker.name(),
                "genre" : random.choice(["action", "comedy", "drama", "fantasy", "documentry"]),
                "director" : faker.name(),
                "year": random.randint(1970, 2023),
                "lenght":random.randint(65,84) * 60 ,
                "studio": faker.company(),
                'actors': actors
            }
            DB.movie.append(obj)
    