from m2 import Shoes
from v2 import View

def start():
    View.start_view()
    # Shoes.load_db_from_file() # Не використовувати
    if input("Create (5) shoes pairs ??? Y - type to create / Enter to skip!!   "):
        Shoes.create_fake_shoes()
    data = Shoes.get_all_films()
    View.show_all_films(data)
    View.end_view()
    # Shoes.save_db_in_file() # Не використовувати


if __name__ == "__main__":
    start()