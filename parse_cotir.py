import json
import requests


def parse_cotir():
    URL = "https://www.cbr-xml-daily.ru/daily_json.js"

    r = requests.get(URL)
    print(r.status_code)

    response_dict = r.json()
    valute_dict = response_dict['Valute']
    all_dicts = []
    for value in valute_dict.values():
        dict = {
            'charCode': value['CharCode'],
            'name': value['Name'],
            'nominal': value['Nominal'],
            'privious': value['Previous'],
            'value': value['Value']
        }
        all_dicts.append(dict)

    return all_dicts
