# Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Вывести на экран исходный и отсортированный массивы.

from random import randint


def shake_bubble_sort(sorting_array):
    up = range(len(sorting_array) - 1)
    shake = True

    while shake:
        for indexes in (up, reversed(up)):
            shake = False
            for i in indexes:
                if sorting_array[i] < sorting_array[i + 1]:
                    sorting_array[i], sorting_array[i + 1] = sorting_array[i + 1], sorting_array[i]
                    shake = True

    return sorting_array


START, END, LEN = -100, (100 - 1), 10

array = [randint(START, END) for _ in range(LEN)]

print(array)

print(shake_bubble_sort(array))
