# По введенным пользователем координатам двух точек вывести уравнение прямой, которая проходит через эти точки
# Блок-схема: https://drive.google.com/file/d/12dOqNXKhEcsttA2eJLY1AhJ5InTd-sJz/view?usp=sharing вкладка task_3

print('Введите координаты первой точки: ')
x1 = int(input('x1: '))
y1 = int(input('y1: '))
print('Введите координаты второй точки: ')
x2 = int(input('x2: '))
y2 = int(input('y2: '))

A = y1 - y2
B = x2 - x1
C = x1 * y2 - x2 * y1

print(f'Уравнение прямой - {A}*x + {B}*y + {C} = 0')
