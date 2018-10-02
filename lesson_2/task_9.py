# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и
# сумму его цифр.
# Блок схема: https://drive.google.com/file/d/1ZfegEIu2YbBSza4Gg_49CfT3U-F30_bB/view?usp=sharing  вкладка task_9

natural_numbers_list = []
max_num = 0
max_sum = 0


def sum_figures_in_number(num_):
    sum__ = 0
    while num_ != 0:
        sum__ += num_ % 10
        num_ = num_ // 10
    return sum__


while True:
    user_input = int(input('Введите натуральное число или "0" для окончания ввода: '))
    if user_input == 0:
        break
    natural_numbers_list.append(user_input)

for num in natural_numbers_list:
    sum_ = sum_figures_in_number(num)
    if sum_ > max_sum:
        max_sum = sum_
        max_num = num

print(f'Число из введенных с максимальной суммой цифр: {max_num}, сумма: {max_sum}')
