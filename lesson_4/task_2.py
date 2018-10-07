# Написать два алгоритма нахождения i-го по счёту простого числа. Первый - использовать алгоритм решето Эратосфена.
# Второй - без использования "решета". Проанализировать скорость и сложность алгоритмов.

import timeit
import cProfile


# "Решето Эратосфена", сложность O((n)*(log(log(n))))

# def sift(n):
#     sieve = [i for i in range(n)]
#     sieve[1] = 0
#
#     for i in range(2, n):
#         if sieve[i] != 0:
#             j = i * 2
#             while j < n:
#                 sieve[j] = 0
#                 j += i
#
#     sieve = [i for i in sieve if i != 0]
#     return sieve
#
# print(sift(1000))


# Возможно недопонял условие, но без указанного диапазона поиска в изначальном виде решето не работоспособно, а так как
# по номеру простого числа не зная этого числа указать диапазон безошибочно затруднительно, решил изменить функцию
# будем просеивать порциями пока не дойдем до искомого элемента:

def search_with_sift(n):
    non_primes_set = set()
    i = 1

    while n != 0:
        i += 1

        if i not in non_primes_set:
            for j in range(i * i, n * n, i):
                non_primes_set.add(j)
            n -= 1
    return i


# print(search_with_sift(100))

# Timeit:
# setup = 'from __main__ import search_with_sift'
# print(timeit.timeit('search_with_sift(100)', setup=setup, number=1000))
# 1.4019409488600727

# cProfile:
# cProfile.run('search_with_sift(100)')
# 15641 function calls in 0.003 seconds
# 1    0.002    0.002    0.003    0.003 task_2.py:30(search_with_sift)
# 1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
# 15637    0.001    0.000    0.001    0.000 {method 'add' of 'set' objects}


# Функция с применением линейного поиска, простой вариант. Сложность O(n2)

def prime_by_num(n):
    i = 2
    counter = 0

    while True:
        for d in range(2, i + 1):
            if i % d == 0:
                if i == d:
                    counter += 1
                break

        if counter == n:
            break

        i += 1
    return i

# print(prime_by_num(100))

# Timeit:
# setup = 'from __main__ import prime_by_num'
# print(timeit.timeit('prime_by_num(100)', setup=setup, number=1000))
# 1.0773975393868012

# cProfile:
# cProfile.run('prime_by_num(100)')
# 4 function calls in 0.001 seconds
# 1    0.001    0.001    0.001    0.001 task_2.py:61(prime_by_num)
# 1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}

# Вывод: за две с лишним тысячи лет вспомогательные средства деятельности человека разумного значительно "поумнели",
# чего нельзя сказать про самого человека разумного
