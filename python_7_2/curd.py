from pony.orm import db_session, commit
from models.ADV import Adv
from faker import Faker
import random
faker = Faker()


# Create Update Read Delete
@db_session
def create_record():
    for _ in range(10):
        Adv(name=faker.name(),
            year=random.randint(2010, 2023),
            rating=random.randint(1, 5))
        
@db_session
def set_name(id, new_name):
    adv = Adv[int(id)]
    adv.name = new_name
    commit()

@db_session
def get_all():
    return list(Adv)

@db_session
def delete_adv(id: int):
    del (Adv[int(id)])