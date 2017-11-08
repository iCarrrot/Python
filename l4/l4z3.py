# -*- coding: utf-8 -*-
import re
import string
import collections


class Przetworz_strumien:
    def __init__(self, strumien):
        self.strumien = strumien
        self.lastword = ""

    def __iter__(self):
        for line in self.strumien:
            words = line.split(' ')
            for word in words:
                word = word.strip(',./\'\"\\!@#$%^&*()_=+*`~?><:;{}[]\n\t')
                if not word:
                    continue
                if self.lastword and self.lastword[-1] == '-':
                    word = self.lastword[:-1] + word
                if word[-1] != '-':
                    yield word
                self.lastword = word

        if self.lastword and self.lastword[-1] == '-':
            yield self.lastword


from collections import Counter


def count_all(strlist):
    strlist = [len(x) for x in strlist]
    strlist = Counter(strlist)
    return strlist


def count_word_len(strlist, n):
    return count_all(strlist)[n]


tekst = open('tekst', 'r')
iterator = Przetworz_strumien(tekst)
dictK = count_all(iterator)
od = collections.OrderedDict(sorted(dictK.items()))
print(od)
