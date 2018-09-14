"""Написать декоратор, измеряющий и печатающий время работы функции
(средства измерения выбрать из предлагаемых стандартной бибилиотекой)"""

def timetracker(func):
    "Декоратор, высчитывающий время работы функции"
    import time

    def wrapper(*args, **kwargs):
        t = time.perf_counter()
        res = func(*args, **kwargs)
        print('Время выполнения:', time.perf_counter() - t)
        return res
    return wrapper

@timetracker
def simple_number(n: int =15)->list:
    """
    Функция поиска всех простых чисел в диапазоне от 2 до n
    :param n: верхняя граница диапазона
    :return: список из простых чисел
    """
    numbers = [x for x in range(n+1)] #список от 0 до n
    i = 2 #начинаем цикл с 2
    result = [] #результирующий список простых чисел

    while i < n:
        if numbers[i] != 0:
            result.append(numbers[i])
            for x in range(i, n+1, i):  #откидываем последующие числа, кратные только что добавленному
                numbers[x] = 0
        i += 1
    return result


print(simple_number())
