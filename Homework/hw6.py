"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести
словарь на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

from hw_funcs import hw_read
from functools import reduce

int_headers = ["lectures", "practicals", "lab"]
raw_data = hw_read("hw6")

headers = [i.replace("\n", "") for i in raw_data[0].split(";")]

data = []

# Simple CSV parsing
for entry in raw_data[1:]:
    in_data = {}
    sliced_data = [i.replace("\n", "") for i in entry.split(";")]
    if len(sliced_data) != len(headers):
        continue

    for idx, value in enumerate(sliced_data):
        header = headers[idx]

        if header in int_headers and value != '':
            value = int(value)

        in_data[header] = value
    data.append(in_data)

dictionary = {}

for i in data:
    dictionary[i["name"]] = reduce(lambda a, b: a+b, [i[field] for field in int_headers if i[field] != ''])

print(dictionary)
