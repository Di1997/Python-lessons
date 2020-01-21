# region Task 1
# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и
# строк и сохраните в переменные, выведите на экран.

v_int, v_string, v_bool = 1, "Test", True
print(f"Int: {v_int}, String: {v_string}, Bool: {v_bool}")

in_string1 = input("Enter string: ")
in_int1 = input("Enter integer: ")

print(f"String: {in_string1}, Int: {in_int1}")

in_string2 = input("Enter string: ")
in_int2 = input("Enter integer: ")

print(f"String: {in_string2}, Int: {in_int2}")

print(f"""
End result: 
1) Int: {v_int}, String: {v_string}, Bool: {v_bool}
2) String: {in_string1}, Int: {in_int1}
3) String: {in_string2}, Int: {in_int2}
""")

# endregion

# region Task 2
# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time = input("Enter time (in seconds): ")

try:
    time = int(time)
    seconds = time % 60
    minutes = (time // 60) % 60
    hours = time // 3600

    print(f"{hours:0>2}:{minutes:0>2}:{seconds:0>2}")
except ValueError:
    print("Time is not a number")

# endregion

# region Task 3
# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3
# + 33 + 333 = 369.

try:
    number = int(input("Enter number between 1 and 9: "))

    if 0 < number < 10:
        print(f"Out: {number + number * 11 + number * 111}")
    else:
        print("Number is too big/too small!")
except ValueError:
    print("Invalid number!")

# endregion

# region Task 4
# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл
# while и арифметические операции.

try:
    number = int(input("Enter any positive number: "))

    if number >= 0:
        max_number = 0
        while number > 0:
            if number % 10 > max_number:
                max_number = number % 10

            number //= 10

        print(f"Number is: {max_number}")
    else:
        print("Number must be positive!")
except ValueError:
    print("Invalid number!")

# endregion

# region Task 5
# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
# фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее
# сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

try:
    revenue = int(input("Enter revenue: "))
    cost = int(input("Enter cost: "))

    if revenue >= 0 and cost >= 0:
        if revenue > cost:
            profit = revenue - cost
            print(f"Result: Profit! Amount of profit: {profit}")
            print("Calculating profit for each employee")
            employees = int(input("Enter amount of employees (Number): "))

            if employees > 0:
                print(f"Profit for each employee: {profit // employees}; Profit leftover: {profit % employees}")
            else:
                print("Amount of employees are less than 1!")
        else:
            print("Result: Loss")
    else:
        print("Revenue or cost less than 0!")
except ValueError:
    print("Invalid number!")

# endregion

# region Task 6
# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день
# спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который общий
# результат спортсмена составить не менее b километров. Программа должна принимать значения параметров a и b и
# выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
#
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

try:
    first_day_kilometer = int(input("Enter first day kilometers: "))
    lf_kilometers = int(input("Enter distance that you are looking for (kilometers): "))

    total = first_day_kilometer
    day = 1
    while total < lf_kilometers:
        print(f"Day {day}: {total:.2f} km")
        total += total / 10
        day += 1

    # final print
    print(f"Day {day}: {total:.2f} km\n\n")

    print(f"Result: On day {day}, the result was {total:.2f} km")
except ValueError:
    print("Invalid number!")

# endregion