"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""
class dividebyzero:
    def __str__(self):
        return self.text
class Number(float):
    def __truediv__(self, other):
        if other is not None and not other:
            raise Error
        return Number(float(self) / float(other))

if __name__ == '__main__':
    while True:
        try:
            separator, divisor = map(Number, input("Введите значения через пробел: ").split())
            print(separator / divisor)
        except Error as e:
            print(e)
        except ValueError as e:
            print(e)
