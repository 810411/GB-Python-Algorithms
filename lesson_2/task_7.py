# Написать программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n – любое натуральное число.
# Блок схема: https://drive.google.com/file/d/1ZfegEIu2YbBSza4Gg_49CfT3U-F30_bB/view?usp=sharing  вкладка task_7

n = int(input('Введите натуральное число: '))
right_part = (n * (n + 1)) / 2
left_part = 0

for i in range(n + 1):
    left_part += i

print(f'Левая часть равенства равна {float(left_part)}, правая {right_part}')
print('Результат выполнения равенства:', left_part == right_part)
