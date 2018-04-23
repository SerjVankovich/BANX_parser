# Лучшая функция, сделанная мною когда-либо
from operator import itemgetter


def get_float(string):
    # Меняем все запятые на точки, чтобы привести к 'float'
    string = string.replace(',', '.')
    if ' ' in string:
        string = string.replace(' ', '')

    # Флаг, что была найдена цифра
    after_num = False

    # Первичная строка, в которую будет записываться результат
    form_string = ''

    for letter in string:
        try:
            # m - неиспользуемая переменная
            m = float(letter)
            after_num = True

            # Если цифра, то добавляем в первичную строку
            form_string += letter
        except ValueError:

            # Если не цифра, то точка?
            if after_num and not '.' in form_string and letter == '.':
                form_string += letter

            # Если не точка, то не буква, ли какая? Это нужно для вытаскивания только одного числа
            elif after_num and letter not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                break
    # Проверка, присутствует ли число в строке вообще?
    try:
        return float(form_string)
    except ValueError:
        return None


def del_num(string):
    format_string = ''
    for letter in string:
        if not letter.isdigit() and letter not in [' ', '.', ',']:
            format_string += letter
    return format_string


def isMes(string):
    prom_string = del_num(string)
    if prom_string == 'мес':
        return True
    else:
        return False


def isDay(string):
    prom_string = del_num(string)
    if prom_string in ['дней', 'дня', 'день']:
        return True
    else:
        return False


def isYear(string):
    prom_string = del_num(string)
    return prom_string in ['год', 'года', 'лет']


def sort_dict(list_dict, is_reverse):
    dicts = []
    for dict in list_dict:
        if 'perinrub' in dict.keys():
            dicts.append(dict)
    dicts = sorted(dicts, key=itemgetter('perinrub'), reverse=is_reverse)
    return dicts



