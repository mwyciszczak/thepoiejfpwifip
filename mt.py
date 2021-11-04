from multiprocessing.pool import Pool
import random
import os

# Chuj mnie to boli

amount = 8
elements = 1000000
t = [[random.randint(0, 1000) for x in range(elements)] for y in range(amount)]


def sort_func(x):
    return sorted(x)


def par_sort(threads, tab):
    with Pool(threads) as p:
        return p.map(sort_func, tab)


x = par_sort(os.cpu_count(), t)
print(x)
#8.85
