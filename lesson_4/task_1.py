# Проанализировать скорость и сложность одного - трёх любых алгоритмов, разработанных в рамках домашнего задания
# первых трех уроков.

import timeit
import cProfile
from random import randint

# Задача 9 из урока 3, "Найти максимальный элемент среди минимальных элементов столбцов матрицы."

SIZE = 100
matrix = [[randint(0, 100) for _ in range(SIZE)] for _ in range(SIZE)]


# Сложность O(n2), - цикл вложенный в цикл

def max_from_min_in_matrix_col(matrix_):
    max_ = float('-inf')

    for j in range(len(matrix_[0])):
        min_ = matrix_[0][j]

        for i in range(len(matrix_)):
            if matrix_[i][j] < min_:
                min_ = matrix_[i][j]

        if min_ > max_:
            max_ = min_

    return max_


# Timeit из скрипта:
# setup = 'from __main__ import max_from_min_in_matrix_col, matrix'
# print(timeit.timeit('max_from_min_in_matrix_col(matrix)', setup=setup, number=1000))
# 0.44095792992707067

# Timeit из консоли:
# python -m timeit -n 1000 -s "import task_1" "task_1.max_from_min_in_matrix_col(task_1.matrix)"
# 1000 loops, best of 3: 446 usec per loop

# cProfile:
# cProfile.run('max_from_min_in_matrix_col(matrix)')
# 105 function calls in 0.001 seconds
# 1    0.001    0.001    0.001    0.001 task_1.py:16(max_from_min_in_matrix_col)
# 1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
# 101    0.000    0.000    0.000    0.000 {built-in method builtins.len}

# Тенденция сложности:
# print(timeit.timeit('max_from_min_in_matrix_col(matrix)', setup=setup, number=1000))  0.44095792992707067
# print(timeit.timeit('max_from_min_in_matrix_col(matrix)', setup=setup, number=10000))  4.455258918796699
# print(timeit.timeit('max_from_min_in_matrix_col(matrix)', setup=setup, number=100000))  45.16516690448422


# И все то же самое для не очень хорошей реализации этой задачи

# Сложность O(n2) + O(n), - цикл вложенный в цикл плюс цикл

def dumb_max_from_min_in_matrix_col(matrix_):
    minimums_list = matrix[0].copy()

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < minimums_list[j]:
                minimums_list[j] = matrix[i][j]

    maximum_in_minimums = minimums_list[0]

    for num in minimums_list:
        if num > maximum_in_minimums:
            maximum_in_minimums = num

    return maximum_in_minimums

# Timeit из скрипта:
# setup = 'from __main__ import dumb_max_from_min_in_matrix_col, matrix'
# print(timeit.timeit('dumb_max_from_min_in_matrix_col(matrix)', setup=setup, number=1000))
# 0.6729236739808869

# Timeit из консоли:
# python -m timeit -n 1000 -s "import task_1" "task_1.dumb_max_from_min_in_matrix_col(task_1.matrix)"
# 1000 loops, best of 3: 661 usec per loop

# cProfile:
# cProfile.run('dumb_max_from_min_in_matrix_col(matrix)')
# 106 function calls in 0.001 seconds
# 1    0.001    0.001    0.001    0.001 task_1.py:51(dumb_max_from_min_in_matrix_col)
# 1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
# 101    0.000    0.000    0.000    0.000 {built-in method builtins.len}


