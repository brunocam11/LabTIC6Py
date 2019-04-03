import requests
import json
import pandas as pd
import time
from multiprocessing import Process, Pool
import numpy as np


def get_weather(api_url):
    r = requests.get(api_url)
    return r.json()


def import_file(file_path):
    with open(file_path) as json_data:
        d = json.load(json_data)
        return d


def append_city_to_df(city):
    api_url = 'http://api.openweathermap.org/data/2.5/weather?id' \
        f'={city["id"]}&appid=914d0fb2b811eadd0aa84cb68f95264e'

    weather = get_weather(api_url)

    name = weather['name']
    temp = weather['main']['temp']
    humidity = weather['main']['humidity']

    return [name, temp, humidity]


if __name__ == '__main__':
    cities = import_file('city.list.small.json')
    # cities_large = import_file('city.list.json')

    start = time.time()

    p = Pool()
    result = p.map(append_city_to_df, cities)

    data = np.array(result)

    data_frame = pd.DataFrame(result, columns=['City',
                                               'Temperature',
                                               'Humidity'])

    end = time.time()

    print(data_frame)
    print()
    print("%.3f" % (end - start), "seconds")
