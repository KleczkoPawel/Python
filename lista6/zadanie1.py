import math
import trojkat as t
a = int(input())
b = int(input())
c = int(input())
def sprawdz(a=0,b=0,c=0):
    if a+b>c and a+c>b and c+b>=a:
        print('Długości a,b,c mogą tworzyć trójkąt\n',
        'obwód trójkąta to: ',t.obwod(a,b,c),'\n',
        'pole trójkąta to: ',t.pole(a,b,c),'\n',
        'typ trójkąta to: ',t.typ(a,b,c),'\n',
        'rodzaj trójkąta to: ',t.kat(a,b,c))
    else:
        print( 'Długości a,b,c nie mogą tworzyć trójkątu' )
sprawdz(a,b,c)
