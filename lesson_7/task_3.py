# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найти в массиве медиану. Медианой
# называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
# в другой – не больше ее.
# quickselect by Tony Hoare

from random import randint, choice


def quickselect_median(array_):
    if len(array_) % 2 == 1:
        return quickselect(array_, len(array_) / 2)
    else:
        return 0.5 * (quickselect(array_, len(array_) / 2 - 1) +
                      quickselect(array_, len(array_) / 2))


def quickselect(_array, index):
    if len(_array) == 1:
        assert index == 0
        return _array[0]

    pivot = choice(_array)

    lows = [i for i in _array if i < pivot]
    highs = [i for i in _array if i > pivot]
    pivots = [i for i in _array if i == pivot]

    if index < len(lows):
        return quickselect(lows, index)
    elif index < len(lows) + len(pivots):
        return pivots[0]
    else:
        return quickselect(highs, index - len(lows) - len(pivots))


START, END, m = 0, 99, 5

array = [randint(START, END) for _ in range(2 * m + 1)]

print(array)

print(quickselect_median(array))
