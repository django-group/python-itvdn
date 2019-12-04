# Задание 3
# Используя ссылки в конце данного урока, ознакомьтесь с таким средством инкапсуляции как свойства.
# Ознакомьтесь с декоратором property в Python. Создайте класс, описывающий температуру и
# позволяющий задавать и получать температуру по шкале Цельсия и Фаренгейта, причём данные могут
# быть заданы в одной шкале, а получены в другой.

class Temp:

    c = 7
    f = 44.6

    def temperature(self, c_new):
        self.c = c_new
        self.f = self.c*(9/5)+32

    def __str__(self):
        return f'Температура: C {self.c}, F {self.f}'

temp_now = Temp()
temp_now.temperature(float(input('Какая сейчас температура по цельсию? ')))
print(temp_now)