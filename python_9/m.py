import json
import random
from faker import Faker
faker = Faker()


class Article:
    def __init__(self, name, author, symbols_count, publisher, description=None):
        self.name = name
        self.author = author
        self.symbols_count = symbols_count
        self.publisher = publisher
        self.description = description

    def __str__(self):
        return f"{self.name} | {self.author} | {self.symbols_count} | {self.publisher} | {self.description}\n"
    
    @classmethod
    def get_all(cls):
        with open("db2.txt", "r") as f:
            data = f.readlines()
        result = []
        for item in data:
            item = json.loads(item)
            article = Article(item["name"], item["author"], item["symbols_count"], item["publisher"], item["description"])
            result.append(article)
        return result

    @classmethod
    def create_article(cls):
        item = {"name": faker.job(),
                "author": faker.name(),
                "symbols_count": random.randint(100, 500),
                "publisher": faker.domain_name(),
                "description": faker.paragraph(nb_sentences=3)
                }
        with open("db2.txt", "+a") as f:
            json.dump(item, f)
            # f.write("\n")