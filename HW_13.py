# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях. 
# Напишите к ним классы исключения с выводом подробной информации. 
# Поднимайте исключения внутри основного кода. 
# Например нельзя создавать прямоугольник со сторонами отрицательной длины.
from HW_13_exeption import LengthError

class Sides:
    def __set_name__(self, owner, name):
        self.param_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, val):
        if val <= 0:
            raise LengthError(val, 0)


class Rectangle:

    _width = Sides()
    _length = Sides()

    def __init__(self, _length: float, _width: float = None) -> None:
        self._length = _length
        if _width:
            self._width = _width
        else:
            self._width = _length

    def perimetr(self):
        return (self._length + self._width) * 2

    def ploshad(self):
        return self._length * self._width

    def __add__(self, other):
        result = self.perimetr() + other.perimetr()
        _width = self._width + other._width
        lenght = (result // 2) - _width
        return Rectangle(_width, lenght)

    def __sub__(self, other):
        result = self.perimetr() - other.perimetr()
        _width = self._width - other._width
        if _width <= 0:
            raise LengthError(_width, 0)
        lenght = (result // 2) - _width
        if lenght <= 0:
            raise LengthError(lenght, 0)
        return Rectangle(_width, lenght)

    def __repr__(self):
        return f"Rectangle{self._width, self._length}"

    def __eq__(self, other) -> bool:
        return self.ploshad() == other.ploshad()

    def __gt__(self, other) -> bool:
        return self.ploshad() > other.ploshad()

    def __le__(self, other) -> bool:
        return self.ploshad() < other.ploshad()


r1 = Rectangle(-2, 0)
r2 = Rectangle(4, 2)
