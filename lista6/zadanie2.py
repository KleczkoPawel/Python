import SzyfrCezara as s
import string
def cezar():
    print('wybierz działanie: 1-szyfrowanie / 2-deszyfrowanie')
    a=int(input())
    print('Wprowadź tekst')
    tekst=input()
    if a==1:
        print('tekst po zaszyfrowaniu')
        print(s.szyfr(tekst))
    elif a==2:
        print('tekst po odszyfrowaniu')
        print(s.deszyfr(tekst))
cezar()

