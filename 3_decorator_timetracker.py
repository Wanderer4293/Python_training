"""Написать декоратор, измеряющий и печатающий время работы функции
(средства измерения выбрать из предлагаемых стандартной бибилиотекой)"""


def timetracker(func):
    import time

    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        res = func(*args, **kwargs)
        end_time = time.perf_counter() - start_time
        print(func.__name__, 'Время выполнения', end_time)
        return res
    return wrapper


def slow_simple_numbers(n: int = 10000)->list:
    """
    Неоптимизированная функция поиска всех простых чисел в диапазоне от 2 до n
    :param n: верхняя граница диапазона
    :return: список из простых чисел

    >>> print(slow_simple_numbers(10))
    [2, 3, 5, 7]
    >>> print(slow_simple_numbers(100))
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    """
    simple_numbers = []

    for x in range(2, n):
        for each in simple_numbers:
            if x % each == 0:
                break
        else:
            simple_numbers.append(x)
    return simple_numbers


def resheto_eratosfena(n: int = 10000)->list:
    """
    Оптимизированная функция поиска всех простых чисел в диапазоне от 2 до n
    :param n: верхняя граница диапазона
    :return: список из простых чисел

    >>> print(resheto_eratosfena(10))
    [2, 3, 5, 7]
    >>> print(resheto_eratosfena(100))
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    """
    numbers = [x for x in range(n+1)]  # список от 0 до n
    i = 2  # начинаем цикл с 2
    simple_numbers = []  # результирующий список простых чисел

    while i < n:
        if numbers[i] != 0:
            simple_numbers.append(numbers[i])
            for x in range(i, n+1, i):  # обнуляем/откидываем последующие числа, кратные только что добавленному
                numbers[x] = 0
        i += 1
    return simple_numbers


# Применяю декоратор без синтаксиса @ чтобы выполнить доктесты для функций
wrapped_slow_simple_numbers = timetracker(slow_simple_numbers)
wrapped_resheto_eratosfena = timetracker(resheto_eratosfena)

wrapped_slow_simple_numbers(10000)
wrapped_resheto_eratosfena(10000)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=1)
