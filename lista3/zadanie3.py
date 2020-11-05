import math
print('ax^2+bx+c=0')
print('podaj a, b oraz c')
a=int(input())
b=int(input())
c=int(input())
delta = b*b -4*a*c
if(a==0):
    print('a musi być różne od 0')
elif (delta > 0):
    pierw = math.sqrt(delta)
    x1 = (-1*b - pierw)/(a*2)
    x2 = (-1*b + pierw)/(a*2)
    print("x1 :")
    print(x1)
    print("x2 :")
    print(x2)    
elif (delta == 0):
    pierw = math.sqrt(delta)
    x1 = (-1*b - pierw)/(a*2)
    print("x0 :")
    print(x1)
else:
    print('wynik:')
    print("brak rozwiązań")
