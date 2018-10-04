# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

from random import sample

random_array = sample(range(-9, 9), 10)
maximum_in_negative = None
position = 0

for num in random_array:
    if num < 0:
        maximum_in_negative = num
        break

for key, value in enumerate(random_array):
    if 0 > value >= maximum_in_negative:
            maximum_in_negative = value
            position = key

if maximum_in_negative is not None:
    print(f'В массиве {random_array}\n'
          f'максимальный отрицательный элемент {maximum_in_negative} находится на позиции {position}.')
