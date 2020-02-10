"""3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (
должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В
классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (
get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров). """


class Worker:
    def __init__(self, name: str, surname: str, position: str, income: dict):
        self._name = name
        self._surname = surname
        self._position = position

        if "wage" in income.keys() and "bonus" in income.keys():
            self._income = income

        else:
            raise ValueError("Income doesn't contain wage or bonus")


class Position(Worker):
    def __init__(self, name: str, surname: str, position: str, income: dict):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        return f"{self._name} {self._surname}"

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


test_position = Position("TestName", "TestSurname", "TestPosition", {"wage": 123, "bonus": 877})

print(test_position.get_full_name())
print(test_position.get_total_income())
