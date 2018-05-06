import json
from bs4 import BeautifulSoup
import urllib.request
from the_best_functions import get_float


def get_html(link):
    response = urllib.request.urlopen(link)
    return response.read()


def parse(html):
    soup = BeautifulSoup(html, 'html.parser')
    table_titles = soup.find_all('div',
                                 class_='ui-panel-light-beige justify-grid position-relative padding-small padding-left-default padding-right-default')
    titles = []

    complete_vklads = []

    vklads = []
    tables_percents = soup.find_all('table', class_='standard-table')
    for table in tables_percents:
        body = table.find('tbody')
        rows = body.find_all('tr')
        stroks = []
        for row in rows:
            cols = row.find_all('td')
            stroke = []
            for col in cols:
                stroke.append(col.text)
            ok_stroke = stroke[:4]
            stroks.append(ok_stroke)

        vklads.append(stroks)

    for row in table_titles:
        title = row.find('a', class_='font-size-x-large font-bold')
        titles.append(title.text)

    for num in range(len(titles)):
        vklad = {}
        vklad['title'] = titles[num]

        for stroke in vklads[num]:
            if stroke[0] == 'Российский рубль':
                vklad['perinrub'] = get_float(stroke[1])
                vklad['suminrub'] = get_float(stroke[2])
                vklad['srokinrub'] = get_float(stroke[3])
            elif stroke[0] == 'Доллар США':
                vklad['perindollars'] = get_float(stroke[1])
                vklad['sumindollars'] = get_float(stroke[2])
                vklad['srokindollars'] = get_float(stroke[3])
            elif stroke[0] == 'Евро':
                vklad['perineuro'] = get_float(stroke[1])
                vklad['sumineuro'] = get_float(stroke[2])
                vklad['srokineuro'] = get_float(stroke[3])
            elif stroke[0] == 'Китайский юань':
                vklad['perinuan'] = get_float(stroke[1])
                vklad['suminuan'] = get_float(stroke[2])
                vklad['srokinuan'] = get_float(stroke[3])
            elif stroke[0] == 'Канадский доллар':
                vklad['perinkandol'] = get_float(stroke[1])
                vklad['suminkandol'] = get_float(stroke[2])
                vklad['srokinkandol'] = get_float(stroke[3])
            elif stroke[0] == 'Австралийский доллар':
                vklad['perinaudol'] = get_float(stroke[1])
                vklad['suminaudol'] = get_float(stroke[2])
                vklad['srokinaudol'] = get_float(stroke[3])
            elif stroke[0] == 'Фунт стерлингов':
                vklad['perinpound'] = get_float(stroke[1])
                vklad['suminpound'] = get_float(stroke[2])
                vklad['srokinpound'] = get_float(stroke[3])
            elif stroke[0] == 'Японская иена':
                vklad['perinien'] = get_float(stroke[1])
                vklad['suminien'] = get_float(stroke[2])
                vklad['srokinien'] = get_float(stroke[3])
            elif stroke[0] == 'Шведская крона':
                vklad['perinkron'] = get_float(stroke[1])
                vklad['suminkron'] = get_float(stroke[2])
                vklad['srokinkron'] = get_float(stroke[3])

        complete_vklads.append(vklad)

    for vklad in complete_vklads:
        print(vklad)


parse(get_html('http://www.banki.ru/products/deposits/primsotsbank/'))
