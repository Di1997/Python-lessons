"""3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе
инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы методы
перегрузки арифметических операторов: сложение (add()), вычитание (sub()), умножение (mul()), деление (truediv(
)).Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не
целочисленное) деление клеток, соответственно. В методе деления должно осуществляться округление значения до целого
числа.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных
двух клеток.

Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек
двух клеток больше нуля, иначе выводить соответствующее сообщение.

Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих
двух клеток.

Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод
позволяет организовать ячейки по рядам.

Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****.
"""

class Cells:
    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other: 'Cells'):
        if type(other) is not Cells:
            raise TypeError("Can't preform this operation on non-cell types")
        return Cells(self.cells + other.cells)

    def __sub__(self, other: 'Cells'):
        if type(other) is not Cells:
            raise TypeError("Can't preform this operation on non-cell types")
        return Cells(self.cells - other.cells)

    def __mul__(self, other: 'Cells'):
        if type(other) is not Cells:
            raise TypeError("Can't preform this operation on non-cell types")
        return Cells(self.cells * other.cells)

    def __truediv__(self, other: 'Cells'):
        if type(other) is not Cells:
            raise TypeError("Can't preform this operation on non-cell types")
        return Cells(round(self.cells / other.cells))

    def make_order(self, length):
        string = '\n'.join([''.join(['*' for _ in range(length)]) for _ in range(self.cells // length)])

        if self.cells % length > 0:
            string += f'\n{"".join(["*" for _ in range(self.cells % length)])}'

        return string


cell_12 = Cells(12)
add_8 = Cells(5) + Cells(3)
sub_16 = Cells(20) - Cells(4)
mul_12 = Cells(6) * Cells(2)
div_10 = Cells(50) / Cells(5)

assert cell_12.cells == 12
assert add_8.cells == 8
assert sub_16.cells == 16
assert mul_12.cells == 12
assert div_10.cells == 10

print(cell_12.make_order(5))
print("\n")

print(add_8.make_order(3))
print("\n")

print(sub_16.make_order(4))
print("\n")

print(mul_12.make_order(2))
print("\n")

print(div_10.make_order(1))
