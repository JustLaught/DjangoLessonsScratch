import json

data = {}
while True:
    select = int(input('1-add, 2-dell, 3-find, 4-edit, 5-save, 6-load, 7-EXIT: '))

    if select == 1:
        name = input('\nEnter name: ')
        passw = input('\nEnter password: ')
        data[name] = passw
    if select == 2:
        name = input('\nEnter name: ')
        if name in data:
            del data[name]
        else:
            print('Not found!')
    if select == 3:
        name = input('\nEnter name:  ')
    if name in data:
        print('User exists')
    else:
        print('No user')
    if select == 4:
        user = input('\nEnter name: ')
        new_pass = input('\nEnter new password: ')
        if user in data:
            data[user]=new_pass
    if select == 5:
        with open('Data', 'w') as file:
         json.dump(data, file)
    if select == 6:
        with open('Data', 'r') as file:
            data = json.load(file)
    if select == 7:
        break