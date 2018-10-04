# Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять сумму
# введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную
# матрицу.

SIZE_X = 5
SIZE_Y = 4
matrix = []

for j in range(SIZE_Y):
    line = []
    sum_for_line = 0
    for i in range(SIZE_X):
        if i < SIZE_X - 1:
            line.append(int(input(f'Введите число для заполнения элемента [{i},{j}]')))
            sum_for_line += line[i]
        else:
            line.append(sum_for_line)
    matrix.append(line)

for line in matrix:
    print(line)
