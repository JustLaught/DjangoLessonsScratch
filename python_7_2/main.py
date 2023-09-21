from models import Adv
from database import db
from pony.orm import db_session
from curd import create_record, set_name, get_all, delete_adv


db.generate_mapping(create_tables=True)

while True:
    option = int(input("1)Create | 2)Update | 3)Delete | 4)Show ALL | 0)Stop !! Enter:  "))
    if option == 1:
        create_record()
            
    elif option == 2:
       set_name(int(input("Enter ID: ")), input("Enter new name"))

    elif option == 3:
        id = input('Enter user ID to be deleted : ')
        delete_adv(id)

    elif option == 4:
        print(get_all(), sep="\n")      

    elif option == 0:
        break