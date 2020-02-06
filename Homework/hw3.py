"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины
дохода сотрудников.
"""

from hw_funcs import hw_read
from functools import reduce

raw_data = hw_read("hw3")

data = [{"Employee": str(i.split(" ")[0]), "Pay": int(i.split(" ")[1])} for i in raw_data]

for bad in [i["Employee"] for i in data if i["Pay"] > 20000]:
    print(f"This employee needs more work: {bad}")

print(f"Average: {reduce(lambda a,b: a+b, [i['Pay'] for i in data]) / len(data)}")
