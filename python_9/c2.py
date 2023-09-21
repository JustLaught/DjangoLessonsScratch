from m2 import Film
from v2 import View

def start():
    View.start_view()
    Film.create_fake_films()
    data = Film.get_all_films()
    View.show_all_films(data)
    View.end_view()


if __name__ == "__main__":
    start()