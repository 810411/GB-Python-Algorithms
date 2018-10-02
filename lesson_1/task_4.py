# Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ. Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
# Блок-схема: https://drive.google.com/file/d/12dOqNXKhEcsttA2eJLY1AhJ5InTd-sJz/view?usp=sharing вкладка task_4

import random

begin = input('Введите начало диапозона: ')
end = input('Введите конец диапозона: ')

if begin.isdigit():
    begin = int(begin)
    end = int(end)
    result = random.randint(begin, end)
elif begin.isalpha():
    begin = ord(begin)
    end = ord(end)
    result = chr(random.randint(begin, end))
else:
    begin = float(begin)
    end = float(end)
    result = random.uniform(begin, end)
print(f'Случайное значение в вашем диапозоне - {result}')
