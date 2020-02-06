"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об
окончании ввода данных свидетельствует пустая строка.
"""

from hw_funcs import get_file_dir

data = []

fileloc = get_file_dir("hw1")

while True:
    user_input = input("Write anything: ")

    if user_input != "":
        data.append(user_input)
    else:
        break

with open(fileloc, "x") as file:
    file.write("\n".join(data))
