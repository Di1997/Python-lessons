"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""

from hw_funcs import hw_read

data = hw_read("hw2")

print(f"Total amount of lines: {len(data)}")

for idx, line in enumerate(data):
    print(f"Line: {idx+1}, word count: {len(str(line).split(' '))}")
