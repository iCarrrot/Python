# -*- coding: utf-8 -*-
import re
import string


class Przetworz_tekst:
    def __init__(self, nazwa):
        self.slowa = []
        self.strumien = open(nazwa, 'r')
        for wiersz in self.strumien:
            for slowo in wiersz.split():
                self.slowa.append(slowo)

    def __iter__(self):
        self.indeks = 0
        self.ile_slow = dict()
        self.poprzednie_slowo = ""
        return self

    def znak_inter(self, x):
        if x in ['.', ',', ';', '...', '!', '?', ':', '(', ')']:
            return True
        return False

    def dodaj_slowo(self, slowo):
        dlugosc = len(slowo)

        if dlugosc not in self.ile_slow:
            self.ile_slow[dlugosc] = 1
        else:
            self.ile_slow[dlugosc] += 1

    def next(self):
        if self.indeks == len(self.slowa):
            self.strumien.close()
            raise StopIteration()

        wynik = self.poprzednie_slowo + self.slowa[self.indeks]
        self.poprzednie_slowo = ""
        self.indeks += 1

        if wynik[-1] == '-':
            self.poprzednie_slowo = wynik[:-1]
            return next(self)

        else:
            regex = re.compile('[^A-Za-ząśćżźóęłńĘÓĄŚŁŻŹĆŃ]')
            wynik = regex.sub('', wynik)

            self.dodaj_slowo(wynik)
            if wynik == '':
                return next(self)
            else:
                return wynik

    def licz_slowa(self):
        self.ile_slow[0]=0
        return self.ile_slow


tekst = Przetworz_tekst("tekst")

print("Lista slow:")
for slowo in tekst:
    print slowo
print "\n"

# for i in range(1, 11):
#  print("Slow dlugosci {}: {}".format(i, tekst.licz_slowa(i)))
# print tekst.licz_slowa()
for i in tekst.licz_slowa():
    print "Słów długości ", i, "\tjest ", tekst.licz_slowa()[i]
