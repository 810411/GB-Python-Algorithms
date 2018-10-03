# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import randint

matrix = []

for i in range(4):
    line = [randint(0, 9) for _ in range(4)]
    matrix.append(line)

minimums_list = matrix[0].copy()

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] < minimums_list[j]:
            minimums_list[j] = matrix[i][j]

maximum_in_minimums = minimums_list[0]

for num in minimums_list:
    if num > maximum_in_minimums:
        maximum_in_minimums = num

print('В матрице:')
for line in matrix:
    print(line)
print(f'максимальный элемент среди минимальных элементов столбцов равен {maximum_in_minimums}.')
