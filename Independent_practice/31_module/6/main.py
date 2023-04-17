import requests
import json

my_reg = requests.get('https://swapi.dev/api/planets/1/')

data = json.loads(my_reg.text)
print(data)

