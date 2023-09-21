class View:
    @classmethod
    def show_all_view(cls, data :list):
        for item in data:
            print(item)

    @classmethod
    def start_viev(cls):
        print("Article archive MVC pattern\n")

    @classmethod
    def end_view(cls):
        print("End in article archive!")