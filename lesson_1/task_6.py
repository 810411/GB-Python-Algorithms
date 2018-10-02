# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
# Блок-схема: https://drive.google.com/file/d/12dOqNXKhEcsttA2eJLY1AhJ5InTd-sJz/view?usp=sharing вкладка task_6

num = input('Введите номер строчной буквы латинского алфавита: ')

letter = chr(int(num) + ord('a') - 1)

print(f'Буква по введенному номеру: {letter}')
