# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

from random import uniform


def merge(left_part, right_part):
    array_ = []
    while left_part and right_part:
        if left_part[0] < right_part[0]:
            array_.append(left_part.pop(0))
        else:
            array_.append(right_part.pop(0))
    if left_part:
        array_.extend(left_part)
    if right_part:
        array_.extend(right_part)
    return array_


def merge_sort(sorting_array):
    array_len = len(sorting_array)
    if array_len >= 2:
        half = int(array_len / 2)
        sorting_array = merge(merge_sort(sorting_array[:half]), merge_sort(sorting_array[half:]))
    return sorting_array


START, END, LEN = 0, 50, 10

array = [uniform(START, END) for _ in range(LEN)]

print(array)

print(merge_sort(array))
