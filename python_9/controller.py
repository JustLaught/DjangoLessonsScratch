import view
from model import Person


def start():
    view.start_view()
    choice = input()
    if choice == "y":
        data = Person.get_all_persons()
        view.show_all_view(data)
        return
    else: return view.last_view()


if __name__ == "__main__":
    Person.create_fake_users()
    start()