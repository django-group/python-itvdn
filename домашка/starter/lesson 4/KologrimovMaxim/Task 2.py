#Задание 2
#Факториалом числа n называется число n! = 1*2*3...*n. Создайте программу, которая
#вычисляет факториал введённого пользователем числа.

n = int(input('Введите число, факториал которого нужно вычислить: '))
fact = 1

for x in range(2, n+1):
    #print(f'Число x = {x}')
    fact = fact*x
    #print(f'fact = {fact}')
else:
    print(f'Факториал числа n: {fact}')