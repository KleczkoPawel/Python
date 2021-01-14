import SzyfrCezara as s
import string
import datetime
import os
import sys
def cezar():
    print('Podaj sciezke bezwzgledna pliku do zaszyfrowania :')
    sciezka = input()
    try:
        plik = open(sciezka,"r+")
    except :
        print('Nie znaleziono pliku')
       # sys.exit(0)

    print('Podaj klucz przesunięcia :')
    klucz = int(input())
    print('Podaj lokalizację katalogu do zapisu pliku zaszyfrowanego')
    sciezkado = input()

    kluczstr = str(klucz)
    sz = ""

    try:
        b = plik.read()
    except:
        print('Błąd odczytu pliku')
        sys.exit(0)


    for c in b:
        c = s.szyfr(c,klucz)
        sz += c

    plik.seek(0)
    plik.write(sz)

    Y = str('{:02d}'.format(datetime.datetime.now().year))
    m = str('{:02d}'.format(datetime.datetime.now().month))
    d = str('{:02d}'.format(datetime.datetime.now().day))

    if os.path.isdir(sciezkado):
        os.rename(sciezka,sciezkado+'/plik_zaszyfrowany%'+kluczstr+'%'+Y+'%'+m+'%'+d)
    else:
        h = "folder_szyfr"
        for i in range(1,100):
            if os.path.exists("folder_szyfr" or "folder_szyfr"+str(i)):
                h = "folder_szyfr"+str(i+1)
                if (os.path.exists(h)==False):
                    break

        os.mkdir(h)
        os.rename(sciezka,h+'/plik_zaszyfrowany%'+kluczstr+'%'+Y+'%'+m+'%'+d)
    plik.close()
cezar()