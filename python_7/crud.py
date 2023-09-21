# CRUD - Create, Read, Update, Delete
from pony.orm import db_session, select, flush, commit
from models import User, Posts
from faker import Faker

fake = Faker()

# @db_session
def create_user():
    with db_session:
        for _ in range(10):
            User(first_name=fake.first_name(), 
                 last_name=fake.last_name(), 
                 age=fake.random_int(18, 99), 
                 email=fake.ascii_free_email())
            
@db_session
def create_posts():
    users = User.select()
    for u in users:
        Posts(title=fake.name(),
            body=" ".join(fake.paragraphs()),
            user=u)

@db_session
def delete_user(id):
    # u = User.select(lambda user: user.id == id)
    u = User[id]
    u.delete()

@db_session
def set_name(id, new_name):
    u = User[id]
    u.first_name = new_name
    u.last_name = "Test"
    u.age = 15
    commit()