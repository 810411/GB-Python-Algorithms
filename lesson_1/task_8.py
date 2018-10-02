# Определить, является ли год, который ввел пользователем, високосным или невисокосным.
# Блок-схема: https://drive.google.com/file/d/12dOqNXKhEcsttA2eJLY1AhJ5InTd-sJz/view?usp=sharing вкладка task_8

year = int(input('Введите год: '))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('Год високосный')
else:
    print('Год невисокосный')
