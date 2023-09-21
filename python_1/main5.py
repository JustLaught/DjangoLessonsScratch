import pickle

class Test:
    a = 15
    b = "sample string"

    def func(self, x):
        print("function func() with argument x = ", x)


with open("data2.pickle", "wb") as file:
    pickle.dump(Test, file)

with open("data2.pickle", "rb") as file:
    NewClass = pickle.load(file)

test_obj = NewClass()
print(test_obj.a)
print(test_obj.b)
test_obj.func(30)
