from database import db
from pony.orm import db_session
from models import User, Book, Posts
from crud import create_user, delete_user, set_name, create_posts


db.generate_mapping(create_tables=True)

# create_user()
# delete_user(15)
# set_name(10, "Test")
# create_posts()
# create_posts()
while True:
    option = int(input("1)Create | 2)Update | 3)Delete | 4)Show ALL | 0)Stop !! Enter:  "))
    if option == 1:
        with db_session:
            User(first_name=input("Enter first name:  "), 
                 last_name=input("Enter last name:  "), 
                 age=int(input("Enter age:  ")), 
                 email=input("Enter email:  "))
            
    elif option == 2:
        with db_session:
            id = int(input("Enter users id:  "))
            u = User[id]
            u.first_name=input("Enter first name:  ") 
            u.last_name=input("Enter last name:  ")
            u.age=int(input("Enter age:  "))
            u.email=input("Enter email:  ")

    elif option == 3:
        with db_session:
            id = input('Enter user ID to be deleted : ')
            User[id].delete()

    elif option == 4:
        with db_session:
            # u = User.select(lambda user: user.age > 40)
            p = Posts.select(lambda posts: posts.user.first_name == "Gary")
            u = User.select(lambda user: user.id == p.user)
            for i in p:
                print(i.to_dict(), sep="\n")  # print(i.to_dict(), sep="\n")  OPTIONAL

    elif option == 0:
        break