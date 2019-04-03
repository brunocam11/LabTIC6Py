import requests
import json
import pandas as pd
import time


def get_weather(api_url):
    r = requests.get(api_url)
    return r.json()


def import_file(file_path):
    with open(file_path) as json_data:
        d = json.load(json_data)
        return d


if __name__ == '__main__':

    cities = import_file('city.list.small.json')
    df = pd.DataFrame(columns=['City', 'Temperature', 'Humidity'])

    start = time.time()
    for i, city in enumerate(cities):
        api_url = 'http://api.openweathermap.org/data/2.5/weather?id' \
                f'={city["id"]}&appid=914d0fb2b811eadd0aa84cb68f95264e'

        weather = get_weather(api_url)

        name = weather['name']
        temp = weather['main']['temp']
        humidity = weather['main']['humidity']

        df.loc[i] = [name, temp, humidity]

    end = time.time()

    print(df)
    print()
    print("%.3f" % (end - start), "seconds")
