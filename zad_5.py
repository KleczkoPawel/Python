import random

def funkcja():
    petla = 0
    punkty = 0

    a = random.randint(1111,4444)

    a_str = str(a)
    a_list = list(a_str)

    print(a)

    zgadnij = list(input())

    for x in range(4):

        if zgadnij[x] in a_str and zgadnij[x] == a_list[x]:
            punkty=punkty+10

        elif a_list[x] in zgadnij and zgadnij[x] != a_list[x]:
            punkty = punkty+1
    print('punkty: ',punkty)  

funkcja()


# Poprzednia wersja
'''
def funkcja():
    p=0
    punkty = 0
    #a = random.randint(1111,4444)
    a = random.randint(1,4)
    b = random.randint(1,4)
    c = random.randint(1,4)
    d = random.randint(1,4)
    while(p==0):
        zgadnij = input()
        zgad = [int(x) for x in str(zgadnij)]
        if a==zgad[0] and b==zgad[1] and c==zgad[2] and d==zgad[3]:
            p=p+1
            print('Gratulacje, udało Ci się')
        elif (a==zgad[0] and b==zgad[1] and c==zgad[2]) or (b==zgad[1] and c==zgad[2] and d==zgad[3]) or (a==zgad[0] and b==zgad[1] and d==zgad[3]) or (a==zgad[0] and d==zgad[3] and c==zgad[2]):
            punkty=punkty+30
            print('punkty: ',punkty) 
        elif (a==zgad[0] and b==zgad[1]) or (b==zgad[1] and c==zgad[2]) or (c==zgad[2] and d==zgad[3]) or (a==zgad[0] and d==zgad[3]) or (a==zgad[0] and c==zgad[2])or (b==zgad[1] and d==zgad[3]):
            punkty=punkty+20
            print('punkty: ',punkty)  
        elif a==zgad[0] or b==zgad[1] or c==zgad[2] or d==zgad[3]:
            punkty=punkty+10
            print('punkty: ',punkty)  
funkcja()'''