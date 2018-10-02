# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых чисел
# и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
# Блок схема: https://drive.google.com/file/d/1ZfegEIu2YbBSza4Gg_49CfT3U-F30_bB/view?usp=sharing  вкладка task_8

initial_num = int(input('Введите число: '))
searching_num = int(input('Введите цифру которую нужно найти в исходном числе: '))
count = 0

while initial_num != 0:
    if initial_num % 10 == searching_num:
        count += 1
    initial_num = initial_num // 10

print(f'Цифра встретилась в числе {count} раз(а)')
