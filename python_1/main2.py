import json


with open("data.json", "r") as file:
    donut_obj = json.load(file)

# print(donut_obj)
for elem in donut_obj["topping"]:
    del elem["type"]

with open("result.json", "w") as file:
    json.dump(donut_obj, file, indent=2)

# print(donut_obj)