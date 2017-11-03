import sys
sys.path.insert(0, '/home/michal/Python/l3')
from z1 import pierwsze_skladana, pierwsze_funkcyjna


def pierwsze_iterator(n):
    pierwsze = []
    if n < 2:
        return pierwsze
    pierwsze += [2]
    for i in range(2, n + 1):
        straznik = 1
        for j in pierwsze:
            if i % j == 0:
                straznik = 0
                break
        if straznik:
            pierwsze += [i]

    return pierwsze


import time

times = [10, 100, 1000, 5000, 10000]

print '\t', '|', 'iterator\t', '|', 'funkcyjna', '\t|', 'skladana'
for i in times:
    s1 = time.time()
    x = pierwsze_iterator(i)
    e1 = time.time()

    s2 = time.time()
    y = pierwsze_funkcyjna(i)
    e2 = time.time()

    s3 = time.time()
    z = pierwsze_skladana(i)
    e3 = time.time()
    print i, '\t', '|', "%.2f" % ((e1 - s1) * 1000), '\t\t|', "%.2f" % ((e2 - s2) * 1000), '\t\t|', "%.2f" % ((e3 - s3) * 1000)


# print(pierwsze_iterator(11))
# print(pierwsze_funkcyjna(11))
# print(pierwsze_skladana(11))
