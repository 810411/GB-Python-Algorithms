# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import randint

SIZE = 10
array = [randint(-100, 100) for _ in range(SIZE)]
print(array)

# 1 вариант
idx_min = 0
idx_max = 0
for i in range(len(array)):
    if array[i] < array[idx_min]:
        idx_min = i
    elif array[i] > array[idx_max]:
        idx_max = i
print(f'Min = {array[idx_min]} в ячейке {idx_min}; Max = {array[idx_max]} в ячейке {idx_max}')

spam = array[idx_min]
array[idx_min] = array[idx_max]
array[idx_max] = spam
print(array)
