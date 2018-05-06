import requests
from firebase import firebase

API_URL = 'https://api.github.com/search/repositories?q=language:java&sort=stars'

r = requests.get(API_URL)
print(r.status_code)

answer = r.json()

items = answer['items']
result_array = []

for item in items:
    prom_dict = {
        'count': item['stargazers_count'],
        'language': item['language'],
        'description': item['description'],
        'name': item['name']

    }
    result_array.append(prom_dict)
import_dict = {'all_projects': result_array}

firebase = firebase.FirebaseApplication('https://test-d2988.firebaseio.com/')
firebase.put('', 'projects', import_dict)
