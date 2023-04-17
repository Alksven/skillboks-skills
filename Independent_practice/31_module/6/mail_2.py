import json
import requests

# print(swapi.get_film(1))
# Сейчас библиотека не работает, получить начало сюжета можно напрямую

result = requests.get("https://swapi.dev/api/films/1/")

json_dict = json.loads(result.text)
print(json_dict)
