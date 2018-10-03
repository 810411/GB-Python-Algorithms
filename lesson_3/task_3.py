# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
# Абстрагировался, из-за неопределенности по условию, от того что можно поменять один максимальный на один минимальный
# элемент, поменял все встречающиеся равные максимальному на равные минимальному и наоборот.

from random import randint

random_array = [randint(0, 9) for _ in range(10)]
maximum = random_array[0]
minimum = random_array[0]

print(random_array)

for num in random_array:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num

for i in range(0, len(random_array)):
    if random_array[i] == maximum:
        random_array[i] = minimum
    elif random_array[i] == minimum:
        random_array[i] = maximum

print(random_array)
