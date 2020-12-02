import math
def obwod(a=0,b=0,c=0):
    return a+b+c
def pole(a=0,b=0,c=0):
    return (math.sqrt(((a+b+c)*(a+b-c)*(a-b+c)*(-a+b+c))/4))/2
def typ(a=0,b=0,c=0):
    if a==b and a==c:
        return 'trójkąt równoboczny'
    elif a==b and a!=c:
        return 'trójkąt równoramienny'
    elif a==c and a!=b:
        return 'trójkąt równoramienny'
    elif b==c and b!=a:
        return 'trójkąt równoramienny'
    else:
        return 'trójkąt różnoboczny'
def kat(a=0,b=0,c=0):
    if a*a+b*b>c*c and b*b+c*c>a*a and a*a+c*c>b*b:
        return 'trójkąt ostrokątny'
    elif a==b==c:
        return 'trójkąt ostrokątny'
    elif c*c==b*b+a*a or b*b==a*a+c*c or a*a==b*b+c*c:
        return 'trójkąt prostokątny'
    elif a*a+b*b<c*c or b*b+c*c<a*a or a*a+c*c<b*b:
        return 'trójkąt rozwartokątny'
    

    