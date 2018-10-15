# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех
# уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Для анализа возьмите любые 1-3 ваших программы. Результаты анализа вставьте в виде комментариев к коду.
# P.S. Напишите в комментариях версию Python и разрядность ОС.
# Python 3.6.5 | 64 bit

import sys


# Функция подсчета размера объекта
def show_size_obj(x, level=0):
    sum_size = sys.getsizeof(x)
    print('\t' * level, f'type = {x.__class__}, size = {sys.getsizeof(x)}, object = {x}')

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for y in x.items():
                sum_size += show_size_obj(y, level + 1)

        elif not isinstance(x, str):
            for y in x:
                sum_size += show_size_obj(y, level + 1)

    if level == 0:
        print(f'Суммарный объем памяти для объекта равен {sum_size} байт')
    return sum_size


# Функция подсчета размера объектов в передаваемой функции
def show_size_func(f):
    sum_size = 0
    for key, x in f.items():
        print(f'Объект в переменной "{key}":')
        sum_size += show_size_obj(x)
    print(f'Суммарный объем памяти для объектов функции равен {sum_size} байт')


# Урок 3 задача 1:

def les_3_task_1():
    result_counter = [0] * 8

    for key, divisor in enumerate(range(2, 10)):
        for number in range(2, 100):
            if number % divisor == 0:
                result_counter[key] += 1
        print(f'В диапазоне натуральных чисел от 2 до 99: {result_counter[key]} чисел кратных {divisor}.')

    return locals()

show_size_func(les_3_task_1())

# Объект в переменной "number":
#  type = <class 'int'>, size = 28, object = 99
# Суммарный объем памяти для объекта равен 28 байт
# Объект в переменной "divisor":
#  type = <class 'int'>, size = 28, object = 9
# Суммарный объем памяти для объекта равен 28 байт
# Объект в переменной "key":
#  type = <class 'int'>, size = 28, object = 7
# Суммарный объем памяти для объекта равен 28 байт
# Объект в переменной "result_counter":
#  type = <class 'list'>, size = 128, object = [49, 33, 24, 19, 16, 14, 12, 11]
# 	 type = <class 'int'>, size = 28, object = 49
# 	 type = <class 'int'>, size = 28, object = 33
# 	 type = <class 'int'>, size = 28, object = 24
# 	 type = <class 'int'>, size = 28, object = 19
# 	 type = <class 'int'>, size = 28, object = 16
# 	 type = <class 'int'>, size = 28, object = 14
# 	 type = <class 'int'>, size = 28, object = 12
# 	 type = <class 'int'>, size = 28, object = 11
# Суммарный объем памяти для объекта равен 352 байт
# Суммарный объем памяти для объектов функции равен 436 байт


# Урок 3 задача 9:

def les_3_task_9():
    from random import randint

    SIZE = 5
    matrix = [[randint(0, 100) for _ in range(SIZE)] for _ in range(SIZE)]

    for line in matrix:
        print(*line, sep='\t')

    max_ = float('-inf')

    for j in range(len(matrix[0])):
        min_ = matrix[0][j]

        for i in range(len(matrix)):
            if matrix[i][j] < min_:
                min_ = matrix[i][j]

        if min_ > max_:
            max_ = min_

    print(f'максимальный элемент среди минимальных элементов столбцов равен {max_}.')

    return locals()

show_size_func(les_3_task_9())

# Объект в переменной "i":
#  type = <class 'int'>, size = 28, object = 4
# Суммарный объем памяти для объекта равен 28 байт
# Объект в переменной "min_":
#  type = <class 'int'>, size = 28, object = 38
# Суммарный объем памяти для объекта равен 28 байт
# Объект в переменной "j":
#  type = <class 'int'>, size = 28, object = 4
# Суммарный объем памяти для объекта равен 28 байт
# Объект в переменной "max_":
#  type = <class 'int'>, size = 28, object = 38
# Суммарный объем памяти для объекта равен 28 байт
# Объект в переменной "line":
#  type = <class 'list'>, size = 128, object = [11, 13, 23, 23, 87]
# 	 type = <class 'int'>, size = 28, object = 11
# 	 type = <class 'int'>, size = 28, object = 13
# 	 type = <class 'int'>, size = 28, object = 23
# 	 type = <class 'int'>, size = 28, object = 23
# 	 type = <class 'int'>, size = 28, object = 87
# Суммарный объем памяти для объекта равен 268 байт
# Объект в переменной "matrix":
#  type = <class 'list'>, size = 128, object = [[30, 100, 45, 22, 38], [16, 29, 93, 62, 94], [73, 68, 3, 15, 62],
# [92, 100, 88, 47, 75], [11, 13, 23, 23, 87]]
# 	 type = <class 'list'>, size = 128, object = [30, 100, 45, 22, 38]
# 		 type = <class 'int'>, size = 28, object = 30
# 		 type = <class 'int'>, size = 28, object = 100
# 		 type = <class 'int'>, size = 28, object = 45
# 		 type = <class 'int'>, size = 28, object = 22
# 		 type = <class 'int'>, size = 28, object = 38
# 	 type = <class 'list'>, size = 128, object = [16, 29, 93, 62, 94]
# 		 type = <class 'int'>, size = 28, object = 16
# 		 type = <class 'int'>, size = 28, object = 29
# 		 type = <class 'int'>, size = 28, object = 93
# 		 type = <class 'int'>, size = 28, object = 62
# 		 type = <class 'int'>, size = 28, object = 94
# 	 type = <class 'list'>, size = 128, object = [73, 68, 3, 15, 62]
# 		 type = <class 'int'>, size = 28, object = 73
# 		 type = <class 'int'>, size = 28, object = 68
# 		 type = <class 'int'>, size = 28, object = 3
# 		 type = <class 'int'>, size = 28, object = 15
# 		 type = <class 'int'>, size = 28, object = 62
# 	 type = <class 'list'>, size = 128, object = [92, 100, 88, 47, 75]
# 		 type = <class 'int'>, size = 28, object = 92
# 		 type = <class 'int'>, size = 28, object = 100
# 		 type = <class 'int'>, size = 28, object = 88
# 		 type = <class 'int'>, size = 28, object = 47
# 		 type = <class 'int'>, size = 28, object = 75
# 	 type = <class 'list'>, size = 128, object = [11, 13, 23, 23, 87]
# 		 type = <class 'int'>, size = 28, object = 11
# 		 type = <class 'int'>, size = 28, object = 13
# 		 type = <class 'int'>, size = 28, object = 23
# 		 type = <class 'int'>, size = 28, object = 23
# 		 type = <class 'int'>, size = 28, object = 87
# Суммарный объем памяти для объекта равен 1468 байт
# Объект в переменной "randint":
#  type = <class 'method'>, size = 64, object = <bound method Random.randint of <random.Random object
# at 0x000002098CC4EA78>>
# Суммарный объем памяти для объекта равен 64 байт
# Объект в переменной "SIZE":
#  type = <class 'int'>, size = 28, object = 5
# Суммарный объем памяти для объекта равен 28 байт
# Суммарный объем памяти для объектов функции равен 1940 байт
