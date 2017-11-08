import time


def test(f, n, k=1000):
    t0 = time.time()
    for i in range(k):
        f(n)
    t1 = time.time()
    avg = (t1 - t0) / k

    print("Average Time Taken", avg)


def pierwsze_skladana(n):
    return [x for x in range(2, n) if all([x % y != 0 for y in range(2, int(x**0.5 + 1))])]


def pierwsze_funkcyjna(n):
    return list(filter(lambda x: all(map(lambda y: x % y != 0, range(2, int(x**0.5 + 1)))), range(2, n)))


# print(timeit.timeit('pierwsze_skladana(100)',number=10000))

if __name__ == '__main__':
    test(pierwsze_skladana, 1000)
    test(pierwsze_funkcyjna, 1000)

    print(pierwsze_funkcyjna(100))
