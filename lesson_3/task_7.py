# В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
# (оба являться минимальными), так и различаться.

from random import randint

SIZE = 10

random_array = [randint(0, 9) for _ in range(SIZE)]

if random_array[0] > random_array[1]:
    min_idx_1 = 0
    min_idx_2 = 1
else:
    min_idx_1 = 1
    min_idx_2 = 0

for i in range(2, len(random_array)):
    if random_array[i] < random_array[min_idx_1]:
        tmp_idx = min_idx_1
        min_idx_1 = i
        if random_array[tmp_idx] < random_array[min_idx_2]:
            min_idx_2 = tmp_idx

    elif random_array[i] < random_array[min_idx_2]:
        min_idx_2 = i

print(f'В массиве {random_array}\nдва наименьших элемента: {random_array[min_idx_1]}, {random_array[min_idx_2]}.')
