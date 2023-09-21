import pickle

numbers = []
for i in range(5):
  some_num = int(input("Enter your number: "))
  numbers.append(some_num)
  
with open("Numbers", "wb") as file:
  pickle.dump(numbers, file)

with open("Numbers", "rb") as file:
  res = pickle.load(file)

print(res)  