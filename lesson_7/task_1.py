# Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Вывести на экран исходный и отсортированный массивы.

from random import randint


def shake_bubble_sort(array_):
    up = range(len(array_) - 1)
    shake = True

    while shake:
        for indexes in (up, reversed(up)):
            shake = False
            for i in indexes:
                if array_[i] < array_[i + 1]:
                    array_[i], array_[i + 1] = array_[i + 1], array_[i]
                    shake = True

    return array_


START, END, LEN = -100, (100 - 1), 10

array = [randint(START, END) for _ in range(LEN)]

print(array)

print(shake_bubble_sort(array))
