class View:
    @staticmethod
    def start_view():
        print("Welcome to the Password Locker. What would you like to watch?\n")

    @staticmethod
    def show_all_films(data):
        for item in data:
            print(item)

    @staticmethod
    def end_view():
        print("\nThank You for using our services.")