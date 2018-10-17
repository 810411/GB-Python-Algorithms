# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найти в массиве медиану. Медианой
# называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
# в другой – не больше ее.
# quickselect by Tony Hoare

from random import randint, choice


def quickselect_median(sorting_array):
    # if len(array_) % 2 == 1:
        return quickselect(sorting_array, len(sorting_array) / 2)
    # else:
    #     return 0.5 * (quickselect(array_, len(array_) / 2 - 1) +
    #                   quickselect(array_, len(array_) / 2))


def quickselect(sorting_array, index):
    if len(sorting_array) == 1:
        assert index == 0
        return sorting_array[0]

    pivot = choice(sorting_array)

    lows = [i for i in sorting_array if i < pivot]
    highs = [i for i in sorting_array if i > pivot]
    pivots = [i for i in sorting_array if i == pivot]

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
