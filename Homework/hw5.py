"""5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод
draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из
классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
метод для каждого экземпляра."""


class Stationery:
    def __init__(self, title):
        self._title = title

    def draw(self):
        print("Starting drawing")


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Pen {self._title} is drawing")


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Pencil {self._title} is drawing")


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Handle {self._title} is drawing")


stationeries = (Stationery("test"),
                Pen("test2"),
                Pencil("test3"),
                Handle("test4"))

for item in stationeries:
    item.draw()