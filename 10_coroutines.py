"""Скрипт, принимающий на вход json-файл, в котором указанны параметры предметов культурного наследия, и возвращающая
для каждого типа кол-во предметов и среднее значения года создания"""

import json
from collections import namedtuple

Result = namedtuple('Result', 'count average')
data = {}  # json_data into data

with open('10_data_gov_ru.json', 'r', encoding='utf8') as f:
    json_data = json.load(f)


# print(json_data)
"""
json_data - список из словарей (один словарь - один предмет культурного наследия) следующего вида:

[{'global_id': 19666571, 'system_object_id': '7033', 'ID': '7033', 'AISID': '9689', 
  'ObjectNameOnDoc': '<Могила> Мартынова Алексея Васильевича (1868-1934)', 
  'EnsembleNameOnDoc': 'Новодевичье кладбище', 'SecurityStatus': 'объект культурного наследия', 
  'Category': 'регионального значения', 'ObjectType': 'Могила'}, ..., 
 {...}]
"""


def get_year(string: str)->int:
    """
    return the last year(YYYY) detected in a json_data_dict['ObjectNameOnDoc']
    :param string
    :return: integer
    >>> get_year('- Жилой дом для служащих с магазином, 1896 г., гражданский инженер О.Ф.Дидио')
    1896
    """
    c = ''
    for char in string:
        if char.isdigit():
            c += char
    return int(c[-4:])


# subgenerator
def averager():
    total = 0
    count = 0
    average_year = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average_year = total/count
    return Result(count, average_year)


# delegator
def grouper(results, key):
    while True:
        results[key] = yield from averager()


# client code
def client(data):
    results = {}
    for keys, values in data.items():
        group = grouper(results, keys)
        next(group)
        for value in values:
            group.send(value)
        else:
            group.send(None)
    report(results)


# print formatted result
def report(results):
    for key, result in sorted(results.items()):
        print('{:40} {:10} шт   среднее: {:.0f} г '.format(key, result.count, result.average))


#  json-file(json_data) processed into one dictionary(data) in the format presented below

#  data =  {'Могила': [], ... 'Скульптура': []}
for dictionaries in json_data:
    data[dictionaries['ObjectType']] = []


# data =  {'Могила': [1949, 1874,], ... 'Скульптура': [1945]}
for dictionaries in json_data:
    data[dictionaries['ObjectType']].append(get_year(dictionaries['ObjectNameOnDoc']))

if __name__ == '__main__':
    client(data)
    import doctest
    doctest.testmod()
