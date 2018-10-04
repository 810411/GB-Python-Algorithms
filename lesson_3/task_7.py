# В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
# (оба являться минимальными), так и различаться.

from random import randint

random_array = [randint(0, 9) for _ in range(10)]
minimum_one = random_array[0]
minimum_two = random_array[-1]
key_for_first_min = 0

for key, value in enumerate(random_array):
    if value < minimum_one:
        minimum_one = value
        key_for_first_min = key

for i in range(0, len(random_array)):
    if i != key_for_first_min:
        if random_array[i] < minimum_two:
            minimum_two = random_array[i]

print(f'В массиве {random_array}\nдва наименьших элемента: {minimum_one}, {minimum_two}.')
