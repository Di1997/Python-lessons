"""1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно
усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать
скрипт."""

from time import mktime, localtime


class ColorInfo:
    def __init__(self, name: str, duration: int):
        self.__name = name
        self.__duration = duration

    def get_name(self):
        return self.__name

    def get_duration(self):
        return self.__duration


class TrafficLight:
    __states = (ColorInfo("Red", 7),
                ColorInfo("Yellow", 2),
                ColorInfo("Green", 5))

    __colors = []

    def __init__(self):
        self.__step = 0
        self.__init_colors()

    def __init_colors(self):
        for color in self.__states:
            for i in range(color.get_duration()):
                self.__colors.append(color)

    def next_step(self):
        self.__step += 1

    def get_current(self):
        if self.__step < len(self.__colors):
            return self.__colors[self.__step]
        else:
            return None


prev_time = mktime(localtime())
last_color = None

tl = TrafficLight()

while True:
    curr_time = mktime(localtime())

    if curr_time > prev_time:
        prev_time = curr_time

        current = tl.get_current()

        if current is None:
            break

        if last_color != current:
            last_color = current
            print(last_color.get_name())

        tl.next_step()
