# Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
# то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
# Блок схема: https://drive.google.com/file/d/1ZfegEIu2YbBSza4Gg_49CfT3U-F30_bB/view?usp=sharing  вкладка task_2

count_even = 0
count_odd = 0
num = input('Введите число: ')
numeral_lst = [int(i) for i in list(num)]

for num in numeral_lst:
    if num % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

print(f'Четных цифр - {count_even}, нечетных - {count_odd}')
