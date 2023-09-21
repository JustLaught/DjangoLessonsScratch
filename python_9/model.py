import json
from faker import Faker
faker = Faker()

class Person:
    def __init__(self, first_name=None, second_name=None):
        self.first_name = first_name
        self.second_name = second_name

    def __str__(self) -> str:
        return f'{self.first_name} {self.second_name}'

    @staticmethod
    def get_all_persons():
        with open("database.txt", "r") as f:
            data = json.load(f)
        result = []
        for item in data:
            p = Person(item["first_name"], item["second_name"])
            result.append(p)
        return result

    @staticmethod
    def create_fake_users():
        data = []
        for i in range(10):
            item = {"first_name": faker.first_name(),
                    "second_name": faker.last_name()}
            data.append(item)
        with open("database.txt", 'w') as f:
            json.dump(data, f)