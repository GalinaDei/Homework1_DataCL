'''Урок 1. Основы клиент-серверного взаимодействия. Парсинг API

3. Сценарий Foursquare
- Напишите сценарий на языке Python, который предложит пользователю ввести интересующую его категорию 
(например, кофейни, музеи, парки и т.д.).
- Используйте API Foursquare для поиска заведений в указанной категории.
- Получите название заведения, его адрес и рейтинг для каждого из них.
- Скрипт должен вывести название и адрес и рейтинг каждого заведения в консоль.'''


import pandas as pd
import requests
import json

endpoint = "https://api.foursquare.com/v3/places/search"
client_id = "__"
client_secret = "__"

city = input("Введите город: ")
place = input("Введите заведение: ")
params = {
"client_id": client_id,
"client_secret": client_secret,
"near": city,
"query": place
}

headers = {
"Accept": "application/json",
"Authorization": "fsq3V3AFHzvqod5PVkb9j5ptfec29VfLTGG2XbHrQEGC8bI="
}

response = requests.get(endpoint, params=params, headers=headers)
if response.status_code == 200:
    print("Успешный запрос")
    data = json.loads(response.text)
    venues = data["results"]
    print("Количество заведений:", len(venues), '\n')
    for venue in venues:
        try:
            print("Категория:", venue["categories"][0]['name'])
            print("Адрес:", venue["location"]["address"])
            print("Картинка:", f"{venue['categories'][0]['icon']['prefix']}{venue['categories'][0]['icon']['suffix']}")
            related_places = list(venue["related_places"].keys())
            if related_places:
                for i in range(len(related_places)):
                    for k,v in venue['related_places'].items():
                        for i in range(len(v)):
                            print("Related_places:", f'{k}: {v[i]["categories"][0]["name"]}')
            print("\n")

        except KeyError:
            print("No data")
            print("\n")
    
