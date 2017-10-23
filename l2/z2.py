from abc import abstractmethod
from itertools import product


class Formula():

    sign = '?'

    def __str__(self):
        return ' ('+self.formuly[0].__str__() + self.sign +self.formuly[1].__str__()+') '

    @abstractmethod
    def oblicz(self, zmienne):
        pass

    def zmienne(self):
        wynik = set()
        if(type(self.formuly[0]) != bool):
            wynik = wynik | self.formuly[0].zmienne()
        if(type(self.formuly[1]) != bool):
            wynik = wynik | self.formuly[1].zmienne()
        return wynik

    def obliczformuly(self, zmienne):
        wyn1,wyn2=(0,0)
        if type(self.formuly[0]) == bool:
            wyn1 = self.formuly[0]
        else:
            wyn1 = self.formuly[0].oblicz(zmienne)
        if type(self.formuly[1]) == bool:
            wyn2 = self.formuly[1]
        else:
            wyn2 = self.formuly[1].oblicz(zmienne)
        return (wyn1, wyn2)

    def __init__(self, f1, f2):
        self.formuly=[]
        self.formuly.append(f1)
        self.formuly.append(f2)


class Zmienna(Formula):
    def __str__(self):
        return str(self.val)

    def __init__(self, v):
        self.val = v

    def zmienne(self):
        if(type(self.val) != bool):
            return set([self.val])

    def oblicz(self, zmienne):
        if(type(self.val) == bool):
            return val
        else:
            return zmienne[self.val]


class Imp(Formula):
    sign = '=>'

    def oblicz(self, zmienne):
        wyn1, wyn2 = self.obliczformuly(zmienne)
        if wyn1 == False:
            return True
        else:
            return wyn2


class And(Formula):
    sign = '&'

    def oblicz(self, zmienne):
        wyn1, wyn2 = self.obliczformuly(zmienne)
        return wyn1 and wyn2


class Or(Formula):
    sign = '|'

    def oblicz(self, zmienne):
        wyn1, wyn2 = self.obliczformuly(zmienne)
        return wyn1 or wyn2


class Iff(Formula):
    sign = '<=>'

    def oblicz(self, zmienne):
        wyn1, wyn2 = self.obliczformuly(zmienne)
        return ((wyn1 and wyn2) or (not wyn1 and not wyn2))


class Not(Formula):
    sign = '!'

    def __str__(self):
        return self.sign + self.val.__str__()

    def __init__(self, f1):
        self.val = f1

    def zmienne(self):
        return self.val.zmienne()

    def oblicz(self, zmienne):
        if(type(self.val) == bool):
            return not self.val
        else:
            return not self.val.oblicz(zmienne)


def tautologia(formula):
    if type(formula) == bool:
        return formula
    variables = list(formula.zmienne())
    for x in product([True, False], repeat=len(variables)):
        if not (formula.oblicz(dict(zip(variables, list(x))))):
            return False
    return True


n = Zmienna(True)
print(Imp(Zmienna('x'), True))
print(Not(True))
print(Not(Zmienna('x')).oblicz({'x': True}))



print(tautologia(Or(Not(Zmienna('y')), Zmienna('y'))))
