import SzyfrCezara as s
import string
import datetime
import os
import sys
import time
def cezar():
    print('Podaj lokalizację katalogu z plikami do deszyfracji :')
    sciezka0 = input()
    if os.path.isdir(sciezka0)==False:
        print('Nie znaleziono katalogu')
        sys.exit(0)

    listaPlikow = os.listdir(sciezka0)

    for i in listaPlikow:
        sciezka = os.path.join(sciezka0,i)

    plik = open(sciezka,'r+')
    print('Podaj lokalizację katalogu do zapisu pliku zdeszyfrowanego')
    sciezkado = input()
    #print('Podaj klucz przesunięcia (1-10):')
    #klucz = int(input())
    
    #kluczstr = str(klucz)
    sz = ""

    try:
        b = plik.read()
    except:
        print('Błąd odczytu pliku')
        sys.exit(0)


    for c in b:
        c = s.deszyfr(c,klucz)
        sz += c

    plik.seek(0)
    plik.write(sz)
    if os.path.isdir(sciezkado):
        os.rename(sciezka,sciezkado+'/plik_zdeszyfrowany%'+kluczstr+'%'+datetime.datetime.now().strftime("%Y-%m-%d"))
    else:
        os.mkdir("folder1")
        os.rename(sciezka,'folder1/plik_zdeszyfrowany%'+kluczstr+'%'+datetime.datetime.now().strftime("%Y-%m-%d"))
        print('Utworzono nowy folder (folder1)')
        
    plik.close()
    

cezar()