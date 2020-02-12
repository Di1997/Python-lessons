"""2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 +
0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property."""

from abc import abstractmethod, ABC


class Clothing(ABC):
    def __init__(self, name):
        self.name = name

    @property
    @abstractmethod
    def total_cloth(self):
        pass


class Coat(Clothing):
    def __init__(self, name, size):
        super().__init__(name)
        self.__size = size

    @property
    def total_cloth(self):
        return self.__size/6.5 + 0.5


class Costume(Clothing):
    def __init__(self, name, height):
        super().__init__(name)
        self.__height = height

    @property
    def total_cloth(self):
        return 2 * self.__height + 0.3


coat = Coat("Coat", 6.5)
costume = Costume("Costume", 0.35)

print(f"{coat.name}: {coat.total_cloth}")
print(f"{costume.name}: {costume.total_cloth}")