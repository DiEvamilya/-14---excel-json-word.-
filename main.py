# а) Создайте json файл в операционной системе, заполните его данными с сайта
# https://jsonplaceholder.typicode.com/todos/
# б) Прочитайте этот файл в массив python-словарей.
# в) Запишите каждый из этих словарей в отдельный json-файл

import urllib.request
import json

url = "https://jsonplaceholder.typicode.com/todos/"


with urllib.request.urlopen(url) as response:
     a = response.read()

b = json.loads(a)
print(b)
# user_id = body_dict['userId']