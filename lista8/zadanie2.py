import SzyfrCezara as s
import string
import datetime
import os
def cezar():
    print('Podaj lokalizację katalogu z plikami do deszyfracji :')
    while 1:
        sciezka = input()
        try:
            plik = open(sciezka,"r+")
            break
        except :
            print('File not found error')
            print('Podaj poprawną lokalizację katalogu')

    print('Podaj lokalizację katalogu do zapisu pliku zaszyfrowanego')
    sciezkado = input()
    print('Podaj klucz przesunięcia :')
    klucz = int(input())
    
    kluczstr = str(klucz)
    sz = ""

    try:
        b = plik.read()
    except:
        print('Błąd odczytu pliku')


    for c in b:
        c = s.deszyfr(c,klucz)
        sz += c

    plik.seek(0)
    plik.write(sz)
    if os.path.isdir(sciezkado):
        os.rename(sciezka,sciezkado+'/plik_zdeszyfrowany-'+kluczstr+'_'+datetime.datetime.now().strftime("%Y-%m-%d"))
    else:
        os.mkdir("folder1")
        os.rename(sciezka,'folder1/plik_zdeszyfrowany-'+kluczstr+'_'+datetime.datetime.now().strftime("%Y-%m-%d"))
        
    plik.close()


cezar()