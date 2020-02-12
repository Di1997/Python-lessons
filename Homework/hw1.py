"""1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который должен
принимать данные (список списков) для формирования матрицы.

Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д."""

from random import randrange


class Matrix:
    def __init__(self, matrix: list):
        if self.__verify_matrix(matrix):
            self.__matrix = matrix
            self.__width = len(matrix[0])
            self.__height = len(matrix)
        else:
            raise ValueError("Bad matrix!")

    def __str__(self):
        string_list = [', '.join([str(elem) for elem in row]) for row in self.__matrix]
        return "\n".join(string_list)

    def __add__(self, other) -> 'Matrix':
        new_rows = []

        if type(other) is not Matrix:
            raise ValueError("Second item is not a matrix!")

        if other.__height != self.__height or other.__width != self.__width:
            raise ArithmeticError("Can't add uneven matrices!")

        for row_idx, row in enumerate(self.__matrix):
            new_elems = []
            for elem_idx, elem in enumerate(row):
                new_elems.append(elem + other.__matrix[row_idx][elem_idx])

            new_rows.append(new_elems)

        return Matrix(new_rows)

    def __verify_matrix(self, item):
        if type(item) is list:
            row_len = None
            for row in item:
                if type(row) is list:

                    if row_len is None:
                        row_len = len(row)

                    if len(row) != row_len:
                        return False

                    for elem in row:
                        if type(elem) is not int:
                            return False
        return True

    @staticmethod
    def random_matrix(height: int, width: int, max_num: int = 10):
        return Matrix([[randrange(0, max_num) for _ in range(width)] for _ in range(height)])


matrix_1 = Matrix.random_matrix(4, 4)
print(f"{matrix_1} \n")

matrix_2 = Matrix.random_matrix(4, 4)
print(f"{matrix_2} \n")

print(f"{matrix_1 + matrix_2}")
