litery = {"a" : "y", "e" : "i", "i" : "o", "o" : "a", "y" : "e"}
reversed_litery = {value : key for (key, value) in litery.items()}
print('Wprowadz tekst do zaszyfrowania/odszyfrowania :')
tekst = input()
def szyfrowanie(tekst):
    print('Tekst po zaszyfrowaniu :')
    for litera in tekst:
        if litera in litery:
            print(litery[litera],end='')
        else:
            print(litera,end='')
def deszyfrowanie(tekst):
    print('\n','Tekst po deszyfrowaniu :')
    for litera in tekst:
        if litera in reversed_litery:
            print(reversed_litery[litera],end='')
        else:
            print(litera,end='')
szyfrowanie(tekst)
#poprawione

