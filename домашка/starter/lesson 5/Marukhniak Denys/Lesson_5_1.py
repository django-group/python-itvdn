# Задание 1
# Создайте функцию, которая выводит приветствие для пользователя с заданным именем. Если
# имя не указано, она должна выводить приветствие для пользователя с Вашим именем.


def hello(my_name='Den'):
    if name == "":
        print('Hello, Den!')
    else:
        print(f'Hello, {my_name}!')


name = input('What is your name? ')
hello(name)
