"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

from hw_funcs import hw_read, get_file_dir
from functools import reduce
from random import randrange

rand_list = [str(randrange(0, 100)) for _ in range(10)]

with open(get_file_dir("hw5"), "x") as file:
    file.write(" ".join(rand_list))

file_data = hw_read("hw5")

print(f"Result: {reduce(lambda a,b: a+b, [int(i) for i in file_data[0].split(' ') if i.isnumeric()])}")
