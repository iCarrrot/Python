def zaszyfruj(tekst, klucz):
    if klucz>255 or klucz<0:
        return tekst
    else:
        return ''.join([chr(ord(x)^klucz) for x in tekst])

def odszyfruj(szyfr, klucz):
    return zaszyfruj(szyfr,klucz)

print(odszyfruj(zaszyfruj('Python12',7),7))