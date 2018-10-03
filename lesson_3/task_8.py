# Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять сумму
# введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную
# матрицу.

matrix = []

for j in range(4):
    line = []
    sum_for_line = 0
    for i in range(5):
        if i < 5 - 1:
            line.append(int(input(f'Введите число для заполнения элемента [{i},{j}]')))
            sum_for_line += line[i]
        else:
            line.append(sum_for_line)
    matrix.append(line)

for line in matrix:
    print(line)
