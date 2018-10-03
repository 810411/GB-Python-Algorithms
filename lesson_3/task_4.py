# Определить, какое число в массиве встречается чаще всего.
# Абстрагировался, из-за неопределенности по условию, от того что одинаково часто встречаться могут несколько чисел,
# в ответ берется первое встреченное.

from random import randint

random_array = [randint(0, 9) for _ in range(10)]
main_counter = 0
answer = 0

for i in range(0, len(random_array)):
    slave_counter = 0
    for j in range(0, len(random_array)):
        if random_array[i] == random_array[j]:
            slave_counter += 1
    if slave_counter > main_counter:
        main_counter = slave_counter
        answer = random_array[i]

print(f'В массиве {random_array}\nсамое частое число {answer} встречается {main_counter} раз(а).')
