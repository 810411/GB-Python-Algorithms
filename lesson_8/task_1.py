# Определение количества различных подстрок с использованием хеш-функции. Пусть дана строка S длиной N. Например,
# состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке. Для
# решения задачи рекомендую воспользоваться алгоритмом sha1 из модуля hashlib или встроенную функцию hash()

import hashlib
from collections import Counter


def rabin_karp(s, subs):
    len_sub = len(subs)
    h_sub = hashlib.sha1(subs.encode('utf-8')).hexdigest()

    for i in range(len(s) - len_sub + 1):
        if h_sub == hashlib.sha1(s[i:i + len_sub].encode('utf-8')).hexdigest():
            return subs


def all_subs_search_in_str(s):
    c = Counter()
    n = len(s)

    for i in range(1, n + 1):
        for j in range(n):
            if j + i > n:
                break

            c[rabin_karp(s, s[j:j + i])] += 1

    return c


str_ = (input('Введите строку из строчных букв: ')).lower()
all_subs = all_subs_search_in_str(str_)
for key, value in all_subs.items():
    print(f'{key:<{len(str_)}} {value}')
