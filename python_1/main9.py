# import pickle

# class Plain:
#     def __init__(self, bort, type):
#         self.name = bort
#         self.type = type

#     def fly(self):
#         print(f"{self.name} is flying")
#     def landing(self):
#         print(f"{self.name} is landing")
#     def show_info(self):
#         print(f"My bort is {self.name} and I am a {self.type}. ")

# boeng = Plain("Boing 7005", "Passanger Aircraft")
# apach = Plain("Apachie", "Attaking Aircraft")


# with open("PlainData", "wb") as f:
#     pickle.dump(boeng, f)
#     pickle.dump(apach, f)

# try:
#     with open("PlainData", "rb") as f:
#         boeng2 = pickle.load(f)
#         apach2 = pickle.load(f)
# except FileNotFoundError:
#     with open("PlainData", "wb") as f:
#         pass

# boeng2.show_info()
# apach2.show_info()
# apach2.fly()
