# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала для каждого
# предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования
# предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
# Использовать модуль collections.

from collections import Counter, OrderedDict

companies = dict()

company_count = int(input('Введите количество предприятий: '))
if company_count <= 1:
    print('Недостаточно данных для сравнения')
    exit(1)

for i in range(1, company_count + 1):
    companyName = input(f'Введите название предприятия №{i}: ')
    profit = Counter()
    for key in ['I', 'II', 'III', 'IV']:
        value = int(input(f'Введите прибыль за {key} квартал: '))
        profit.update({key: value})
    companies[f'№{i} {companyName}'] = sum(profit.values())

average = sum(companies.values()) / len(companies)
companies['average'] = average
companies = OrderedDict(sorted(companies.items(), key=lambda x: x[1], reverse=True))

print('Предприятия, чья прибыль выше среднего: ')
for key, value in companies.items():
    if key == 'average':
        print('Предприятия, чья прибыль ниже среднего: ')
    if value != average:
        print(f'{key}: {value}')
