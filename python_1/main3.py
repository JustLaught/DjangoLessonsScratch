import json

import requests

url = "https://jsonplaceholder.typicode.com/todos"

response = requests.get(url)
data = json.loads(response.content)

with open("first.json", "wb") as file:
    file.write(response.content)

with open("second.json", "w") as file:
    json.dump(data, file, indent=4)

for elem in data:
    if elem['id'] % 10 == 0:
        print(elem)

# print(json.loads(response.content))