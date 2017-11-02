

def pierwsze_skladana(n):
    pierwsze = [x for x in range(
        2, n + 1) if len([y for y in range(2, int(round(x**(0.5))) + 1) if x % y == 0]) == 0]
    return pierwsze


def pierwsze_funkcyjna(n):
    def foo(x):
        for i in range(2, int(round(x**(0.5))) + 1):
            if x % i == 0:
                return False
        return True

    numerki = range(2, n + 1)
    pierwsze = filter(foo, numerki)
    return pierwsze


def rozklad_skladana(n):
    pierwsze = pierwsze_funkcyjna(n)
    rozklad = [(x, y) for x in pierwsze for y in range(1, n + 1)
               if n % (x**y) == 0 and n % (x**(y + 1)) != 0]
    return rozklad


def rozklad_funkcyjna(n):
    def foo(x):
        for i in range(1, n + 1):
            if n % (x**i) == 0 and n % (x**(i + 1)) != 0:
                return (x, i)
        return None

    pierwsze = pierwsze_funkcyjna(n)
    rozklad = filter(lambda x: x is not None, map(foo, pierwsze))
    return rozklad


l = 756
print (rozklad_skladana(l))
print (rozklad_funkcyjna(l))
