
class LengthError(Exception):

    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def __str__(self):

        if self.a < self.b:
            return f'Сторона прямоугольника не может быть меньше нуля\n' \
                   f'Заданное число { self.a} < {self.b}'
        elif self.a == self.b:
            return f'Сторона прямоугольника не может быть равна нулю\n' \
                   f'Заданное число { self.a} = {self.b}'
