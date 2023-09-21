class View:
    @staticmethod
    def start_view():
        print("Welcome to the Servise Shoes.\n")

    @staticmethod
    def show_all_films(data):
        print()
        for item in data:
            print(item, end="\n")
        

    @staticmethod
    def end_view():
        print("\nThank You for using our services.")