# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
# необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных
# значений необходимо запускать скрипт с параметрами.

from sys import argv as args

if len(args) == 4:

    prod_hours = args[1]
    salary = args[2]
    performance_pay = args[3]

    if prod_hours.isnumeric() and salary.isnumeric() and performance_pay.isnumeric():
        total = int(prod_hours) * int(salary) + int(performance_pay)
        print(f"Result ({int(prod_hours)} * {int(salary)} + {int(performance_pay)}): {total}")
    else:
        print("All arguments must be a number!")

else:
    print("Invalid amount of arguments!")
