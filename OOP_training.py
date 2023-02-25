# Небольшая задачка на ООП. Если все сделано, то можно за нее взяться. На звонке в пятницу на ее примере поговорм про ООП.
# Надо написать классы для треугольника и прямоугольника.
# - Для создания треугольника передаются три стороны,
# для прямоугольника две стороны.
# Также еще передается цвет фигуры.
# - У этих классов должен быть метод который выводит информацию о фигуре,
# что это за фигура и какие у нее параметры и цвет.
# И еще надо реализовать метод покраски - который принимает на вход цвет
# и меняет цвет фигуры на новый.
# Если цвет такой же, то выводится сообщение, что фигура уже такого же цвета.
# - Также у этих классов должны быть методы расчета периметра и площади.


class Figure:

    def __init__(self, a):
        self.a = abs(a)
        self.color = None

    def __repr__(self):
        return str(self.__class__.__name__)

    def set_color(self, color: str):
        if color != self.color and color.isalpha():
            self.color = color
        else:
            print(f'Figure is already {self.color}')

    def info(self):
        all_info = [
            f'Type: {str(self.__class__.__name__)}',
            f'Color: {self.color}',
            f'Side a: {self.a}'
        ]
        return all_info

    def __setattr__(self, key, value):
        if not issubclass(type(self), Figure):
            return None
        else:
            self.__dict__[key] = value


class Triangle(Figure):
    def __init__(self, a, *args):
        super().__init__(a)
        if args and len(args) == 2:
            b = abs(args[0])
            c = abs(args[1])
            if (self.a + b > c and
                    self.a + c > b and
                    b + c > self.a):
                self.b = abs(args[0])
                self.c = abs(args[1])
            else:
                raise ValueError('Impossible triangle')
        else:
            self.b = self.a
            self.c = self.a

    def perimeter(self):
        return self.a + self.b + self.c

    def square(self):
        p = self.perimeter() / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

    def info(self):
        all_info = super().info()
        all_info.append(f'Side b: {self.b}')
        all_info.append(f'Side c: {self.c}')
        all_info.append(f'Perimeter: {self.perimeter()}')
        all_info.append(f'Square: {self.square()}')
        for each in all_info:
            print(each)


class Rectangle(Figure):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b

    def info(self):
        all_info = super().info()
        all_info[2] = f'Side a, c: {self.a}'
        all_info.append(f'Side b, d: {self.b}')
        all_info.append(f'Perimeter: {self.perimeter()}')
        all_info.append(f'Square: {self.square()}')
        for each in all_info:
            print(each)

    def perimeter(self):
        return (self.a + self.b) * 2

    def square(self):
        return self.a * self.b

if __name__ == '__main__':
    print(Triangle(3))
    triangle = Triangle(2, 3, 4)
    print(triangle.perimeter())
    triangle.set_color('green')
    triangle.set_color('green')
    triangle.info()
    rectangle = Rectangle(3, 4)
    rectangle.info()
    print(rectangle.square())