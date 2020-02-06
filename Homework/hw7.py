"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма
собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
убытки, в расчет средней прибыли ее не включать.

Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

from hw_funcs import hw_read, get_file_dir
from functools import reduce
from json import dumps

int_headers = ["revenue", "cost"]
raw_data = hw_read("hw7")

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

result = []

companies = {}

for entry in data:
    companies[entry["name"]] = entry["revenue"] - entry["cost"]

result.append(companies)
result.append({"average_profit": reduce(lambda a, b: a+b, [i for i in companies.values()]) / len(data)})

json_file = get_file_dir("hw7_json")

with open(json_file, "x") as file:
    file.write(dumps(result))
