"""2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета
массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина*ширина*масса асфальта
для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т """


class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calculate(self, mass, thickness):
        return self.__length * self.__width * mass * (thickness / 1000)


print(Road(20, 5000).calculate(25, 5))
