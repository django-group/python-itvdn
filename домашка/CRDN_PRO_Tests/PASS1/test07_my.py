# Створити функцію find_simple(numbers) яка на вхід отримує список цілих невід'ємних чисел і
# на вихід повертає список простих чисел знайдених у вхідному списку. Якщо одне і те ж число повторюється
# у вхідних даних, то воно також має повторюватись і у вихідних. Порядок слідування чисел у вихідних даних
# має бути таким самим як і у вхідних даних
#
# Просте число  — це натуральне число, яке має рівно два різних натуральних дільники (лише 1 і саме число).


def is_simple(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                return False
        return True


def find_simple(numbers):
    s_lst = [x for x in numbers if is_simple(x)]
    return s_lst


print(find_simple(range(10)))
print(find_simple([1, 2, 4, 6, 3, 8, 12, 2, 18, 5, 24, 13]))