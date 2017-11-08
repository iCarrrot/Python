# -*- coding: utf-8 -*-
from l3z1 import pierwsze_skladana, pierwsze_funkcyjna

# sito erastotenesa żeby bylo ciekawiej


def pierwsze_iterator(n):
    pierwsze = range(2, n)
    if not pierwsze:
        return pierwsze
    div = pierwsze[0]
    while div < n**0.5 + 1:
        yield div
        pierwsze = [x for x in pierwsze if x % div != 0]
        div = pierwsze[0]
    for i in pierwsze:
        yield i


if __name__ == "__main__":

    import time

    times = [10, 100, 1000, 10000, 50000]

    print ('\t', '|', 'iterator\t', '|', 'funkcyjna', '\t|', 'skladana')
    for i in times:
        s1 = time.time()
        x = list(pierwsze_iterator(i))
        e1 = time.time()

        s2 = time.time()
        y = pierwsze_funkcyjna(i)
        e2 = time.time()

        s3 = time.time()
        z = pierwsze_skladana(i)
        e3 = time.time()
        print (i, '\t', '|', "%.5f" % ((e1 - s1) * 1000), '\t|', "%.5f" %
               ((e2 - s2) * 1000), '\t|', "%.5f" % ((e3 - s3) * 1000))
