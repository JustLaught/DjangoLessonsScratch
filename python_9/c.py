from m import Article
from v import View


def start():
    # for i in range(15):
    #     Article.create_article()
    data = Article.get_all()
    View.start_viev()
    View.show_all_view(data)
    View.end_view()

if __name__ == "__main__":
    start()