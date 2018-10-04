# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

from random import shuffle

random_array = list(range(10))
shuffle(random_array)
start = 0
stop = 0
sum_between_min_max = 0

for key, value in enumerate(random_array):
    if value > random_array[start]:
        start = key
    if value < random_array[stop]:
        stop = key

if start > stop:
    start, stop = stop, start

for i in range(start + 1, stop):
    sum_between_min_max += random_array[i]

print(f'В массиве {random_array}\n'
      f'cумма элементов массива между максимальным и минимальным равна {sum_between_min_max}.')
