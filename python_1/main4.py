import pickle

json_obj = [
  {
    "userId": 1,
    "id": 1,
    "title": "delectus aut autem",
    "completed": False
  },
  {
    "userId": 1,
    "id": 2,
    "title": "quis ut nam facilis et officia qui",
    "completed": False
  },
  {
    "userId": 1,
    "id": 3,
    "title": "fugiat veniam minus",
    "completed": False
  },
  {
    "userId": 1,
    "id": 4,
    "title": "et porro tempora",
    "completed": True
  }
]

with open("data.pickle", "wb") as file:
    pickle.dump(json_obj, file)

with open("data.pickle", "rb") as file:
    new_obj = pickle.load(file)


for elem in new_obj:
    print(elem)