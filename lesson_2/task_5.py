# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.
# Блок схема: https://drive.google.com/file/d/1ZfegEIu2YbBSza4Gg_49CfT3U-F30_bB/view?usp=sharing  вкладка task_5

lst = []

for i in range(32, 128):
    lst.append(f'«{i:3}-{chr(i)}»')

for i, value in enumerate(lst):
    print(f'{value:7}  ', end='')
    if (i + 1) % 10 == 0 and i != 0:
        print()
