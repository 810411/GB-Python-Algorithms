# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125, ... Количество элементов (n) вводится
# с клавиатуры.
# Блок схема: https://drive.google.com/file/d/1ZfegEIu2YbBSza4Gg_49CfT3U-F30_bB/view?usp=sharing  вкладка task_4

num = 1
result = 0
n = int(input('Введите количество элементов ряда чисел: 1, -0.5, 0.25, -0.125, ... : '))

for i in range(n):
    result += num
    num = (- num) / 2

print(result)
