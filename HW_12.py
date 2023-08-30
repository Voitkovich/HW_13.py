# Задание 1. Создайте класс студента.
# - Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.


class NameValidator:
    def __set_name__(self, owner, name):
        self._name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self._name, None)

    def __set__(self, instance, value):
        if not value.istitle() or not value.isalpha():
            raise ValueError("Имя должно начинаться с заглавной буквы и состоять только из букв.")
        setattr(instance, self._name, value)  



class Student:
    first_name: str = NameValidator()
    middle_name: str = NameValidator()
    last_name: str = NameValidator()

    def __init__(self, first_name, middle_name, last_name):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name  

    def __str__(self):
            return f"Имя {self.first_name}, Фамилия {self.middle_name}, Отчество {self.last_name}"     


std1 = Student('Евлампий', 'Серый', 'Вольфович')
# std2 = Student('dgd', '222', 444)
print(std1)
# print(std2)            