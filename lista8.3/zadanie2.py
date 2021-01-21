import SzyfrCezara as s
import string
import datetime
import os
import sys
import time
def cezar():
    
    print('Podaj lokalizację katalogu z plikami do deszyfracji :')
    sciezka0 = input()

    while True:
        try:
            os.path.isdir(sciezka0)
            break
        except FileNotFoundError:
            print('Nie znaleziono podanego katalogu, podaj poprawną ścieżkę')
        except:
            print('Błąd nieznanego pochodzenia')
            sys.exit(0)
 
    listaPlikow = os.listdir(sciezka0)
    
    for i in listaPlikow:
        if('plik_zaszyfrowany' in i):
            sciezka = os.path.join(sciezka0,i)
            break
        else:
            print('W podanym katalogu nie znaleziono plików do deszyfracji')
            sys.exit(0)

    try:
        plik = open(sciezka,'r+')
    except:
        print('Wystąpił błąd nieznanego pochodzenia')
        plik.close()
        sys.exit(0)

    print('Podaj lokalizację katalogu do zapisu pliku zdeszyfrowanego')
    sciezkado = input()

    tablica_klucz = sciezka.split("%")
    klucz_str = tablica_klucz[1]
    klucz = int(klucz_str)
    zapis = ""

    try:
        odczyt_pliku = plik.read()
    except:
        print('Błąd odczytu pliku')
        plik.close()
        sys.exit(0)


    for litera in odczyt_pliku:
        litera = s.deszyfr( litera, klucz )
        zapis += litera

    plik.seek(0)
    plik.write(zapis)

    Y = str('{:02d}'.format(datetime.datetime.now().year))
    m = str('{:02d}'.format(datetime.datetime.now().month))
    d = str('{:02d}'.format(datetime.datetime.now().day))
    
    try:
        if os.path.isdir( sciezkado ):
            os.rename( sciezka, sciezkado + '/plik_zdeszyfrowany%' + klucz_str + '%' + Y + '%' + m + '%' + d )

                                                        # tworzenie nowego folderu jeżeli ścieżka jest nieprawidłowa
        else:
            nazwa_folderu = "folder_deszyfr"
            for i in range( 1, 100 ):
                if os.path.exists( "folder_deszyfr" or "folder_deszyfr" + str(i) ):
                    nazwa_folderu = "folder_deszyfr" + str(i+1)
                    if ( os.path.exists( nazwa_folderu ) == False ):
                        break
        os.mkdir( nazwa_folderu )
        os.rename( sciezka, nazwa_folderu + '/plik_zdeszyfrowany%' + klucz_str + '%' + Y + '%' + m + '%' + d )
    except:
        plik.close()
        sys.exit(0)
        print('Błąd zapisu katalogu/pliku')   

    plik.close()
    

cezar()