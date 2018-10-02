# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено
# число 3486, то надо вывести число 6843.
# Блок схема: https://drive.google.com/file/d/1ZfegEIu2YbBSza4Gg_49CfT3U-F30_bB/view?usp=sharing  вкладка task_3

result = ''
num = int(input('Введите число: '))

while num != 0:
    result += str(num % 10)
    num = num // 10

print(int(result))
