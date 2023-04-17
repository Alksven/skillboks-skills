import requests
import json

my_reg = requests.get('https://swapi.dev/api/planets/3/')

data = json.loads(my_reg.text)

with open('my_test.json', 'w') as file:
    json.dump(data, file, indent=4)

with open('my_test.json', 'r') as file:
    new_name = json.load(file)
    new_name['name'] = 'Ven'

with open('my_test.json', 'w') as file:
    json.dump(new_name, file, indent=4)

with open('my_test.json', 'r') as file:
    size = json.load(file)
    print(size["url"])