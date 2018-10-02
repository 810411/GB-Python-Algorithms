# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
# Блок-схема: https://drive.google.com/file/d/12dOqNXKhEcsttA2eJLY1AhJ5InTd-sJz/view?usp=sharing вкладка task_5

print('Введите две строчные буквы латинского алфавита')
first = input('Первая буква: ')
second = input('Вторая буква: ')

num_first = ord(first) - ord('a') + 1
num_second = ord(second) - ord('a') + 1

distance = abs(num_first - num_second) - 1

print(f'Порядковый номер первой буквы - {num_first}')
print(f'Порядковый номер второй буквы - {num_second}')
print(f'Расстояние между этими буквами - {distance}')
