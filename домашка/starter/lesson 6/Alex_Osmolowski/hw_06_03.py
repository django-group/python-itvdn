# Задание 3
# Пусть на каждую ступеньку лестницы можно стать с предыдущей или переступив через одну.
# Определите, сколькими способами можно подняться на заданную ступеньку.


def step(x):
    if x == 1 or x == 2:
        return 1
    else:
        return step(x-1) + step(x-2)


n = int(input("Введите количество ступенек: "))

print("Вы можете подняться на {} ступенек {} способами.".format(n, step(n+1)))