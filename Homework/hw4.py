"""4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс
метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении
скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Выполните вызов методов и также покажите результат. """


class Car:
    def __init__(self, speed, color, name, is_police: bool):
        self._speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.__limit = None

    def go(self):
        return f"{self.name} Go!"

    def stop(self):
        return f"{self.name} Stopping"

    def turn(self, direction):
        return f"{self.name} Turning {direction}"

    def _set_limit(self, limit):
        self.__limit = limit

    def show_speed(self):
        return f"{self._speed}\nSpeed over the limit!" if (self.__limit is not None and self._speed > self.__limit) else str(
            self._speed)


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)
        super()._set_limit(60)


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)
        super()._set_limit(40)


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


cars = (TownCar(50, "yellow", "Ok car"),
        TownCar(5000, "yellow", "Bad car"),
        SportCar(600, "red", "Sport car"),
        WorkCar(40, "blue", "Ok work car"),
        WorkCar(50, "blue", "Bad work car"),
        PoliceCar(9001, "black", "MIB car"))

for car in cars:
    print(f"Car name: {car.name}",
          f"Car color: {car.color}",
          f"Car speed: {car.show_speed()}",
          f"Is police car: {car.is_police}",
          f"Going forward: {car.go()}",
          f"Turning left: {car.turn('left')}",
          f"Stopping car: {car.stop()}\n\n", sep="\n")

