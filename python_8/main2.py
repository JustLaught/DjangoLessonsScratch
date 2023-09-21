import redis
import json

r = redis.Redis(
  host='redis-12589.c281.us-east-1-2.ec2.cloud.redislabs.com',
  port=12589,
  username="Test",
  password="Qwer12-=")

def create_user_list():
    r.json().set("users", "$", dict())

def new_user(name, password):
    user = {
        "name": name,
        "password": password,
        "cart": {}
    }

    path = f"$.{name}"
    if len(r.json().get("users", path)) == 0:
        r.json().set("users", path, user)
    else:
        raise "User already exists"
    
def get_user(name):
    u = r.json().get("users", f"$.{name}")[0]
    print(f"User : {u['name']}")
    print(f"Password : {u['password']}")
    print(u['cart'])
    for item, amount in u['cart'].items():
        print(f"Cart item : {item} : {amount}")


def check_password(name, password):
    user_password = r.json().get("users", f"$.{name}.password")[0]
    if user_password == password:
        return True
    else:
        return False

def add_item_to_cart(name, item, amount):
    r.json().set("users", f"$.{name}.cart.{item}", amount)

def del_item_from_cart(name, item):
    r.json().delete("users", f"$.{name}.cart.{item}")

def get_item_from_cart(name, item):
    amount = r.json().get("users", f"$.{name}.cart.{item}")
    if len(amount) > 0:
        return amount[0]
    else:
        return None

def change_item_in_cart(name, old_item, new_item):
    amount = get_item_from_cart(name, old_item)
    if amount is not None:
        add_item_to_cart(name, new_item, amount)
        del_item_from_cart(name, old_item)
    
    # if amount := get_item_from_cart(name, old_item) is not None:
    #     add_item_to_cart(name, new_item, amount)
    #     del_item_from_cart(name, old_item)

def clear_cart(name):
    r.json().set("users", f"$.{name}.cart", {})

# {
#     "name": "User_Name",
#     "password": "qwerty",
#     "cart": {
#         {
#             "product": "product_name",
#             "amount": amount
#         },
#         {
#             "product": "product_2_name",
#             "amount": amount
#         },
#     }
# }

# users = {
#     "Test_user": "qwertru",
#     "Admin": "28371832",
# }

# def new_user_2(name, password):
#     users = json.loads(r.get("users"))
#     if users[name] is None:
#         users[name] = password
#     else:
#         raise "User already exists"
#     r.set("users", json.dumps(users))

# new_user("test_user_1", "asdfgh")

# print(check_password("test_user_1", "asdfgh"))

# create_user_list()

# new_user("Test_user", "test_password")
add_item_to_cart("Test_user", "orange", 3)
add_item_to_cart("Test_user", "banana", 5)
add_item_to_cart("Test_user", "candies", 30)
# del_item_from_cart("Test_user", "orange")
# change_item_in_cart("Test_user",  "apples", "candies")
# clear_cart("Test_user")
get_user("Test_user")

# new_user("Second_user", "pass")

get_user("Second_user")
print(get_item_from_cart("Test_user", "orange"))
print(get_item_from_cart("Second_user", "orange"))

# print(check_password("Test_user", 'test_password'))

# path = f"$.{'Test_user'}"
# print(r.json().get("users", path))
# print(r.json().get("users", "$"))


r.json().get("Second_user", "$")
r.json().set("Third_user", "$", {})
r.json().set("Third_user", "$.cart", {})

r.set("Fourth_user", json.dumps({}))
user = json.loads(r.get("Fourth_user"))


# {
#     "name" : 123,
#     "name" : 123,
#     "name" : 123,
#     "name" : 123,
# }