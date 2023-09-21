import redis
import json
from random import randint


r = redis.Redis(
    host='redis-15398.c10.us-east-1-2.ec2.cloud.redislabs.com', 
    port=15398,
    username="Test",
    password="Qwer13-=")


def get_data():
    data = r.json().get('users')
    print()
    for i in data:
        print(data[i])

def create_user_list():
    if r.json().get("users", "$") is None:
        r.json().set("users", "$", dict())

def create_data(name, password):
    user = {"name" : name,"password" : password, "points": randint(1, 100)}
    if len(r.json().get("users", f"$.{name}")) == 0:
        r.json().set("users", f"$.{name}", user)
    else: print("User w/ this name already exists\nCan`t be 2 same users Sorry!!")

def clear_all_data():
    r.json().delete("users")

def show_by_name(name):
    if len(r.json().get("users", f"$.{name}")) != 0:
        print(r.json().get("users", f"$.{name}"))
    else: print("\nUser not found")

def change_points(name):
    if r.json().get("users", f"$.{name}"):
        r.json().set("users", f"$.{name}.points", int(input("Enter points:  ")))

def top_ten():
    data = r.json().get("users")
    users_list = sorted(data.values(), key=lambda x: x["points"], reverse=True)
    print()
    if len(users_list) < 10:
        for i in users_list:
            print(f"Name: {i['name']} | Points: {i['points']}")
    else:
        for i in range(10):
            print(f"Name: {users_list[i]['name']} | Points: {users_list[i]['points']}")


while True:
    inp = int(input("\n1:Create users list | 2:Create data | 3:Delete ALL data\
\n4:Show ALL users in list | 5:Show User by name | 6:Change points | 7:Top 10\
\n0:Exit | Enter:  "))
    if inp == 1:
        create_user_list()

    elif inp == 2:
        create_data(input("Enter name:  "), input("Enter password:  "))

    elif inp == 3:
        clear_all_data()

    elif inp == 4:
        get_data()

    elif inp == 5:
        show_by_name()
    
    elif inp == 6:
        change_points(input("Enter name:  "))
        
    elif inp == 7:
        top_ten()
    
    elif inp == 0:
        break