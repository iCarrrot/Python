l = 11


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


print (pierwsze_skladana(l))
print (pierwsze_funkcyjna(l))
