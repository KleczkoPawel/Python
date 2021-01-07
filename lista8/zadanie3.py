import random


def generatepesel():
    rok = random.randint(1900, 2099)
    if rok < 2000:
        miesiac = "%02d"%random.randint(1,12)
    else:
        miesiac = int("%02d"%random.randint(1, 12))+20

    if int(miesiac)%2==0:
        dzien = "%02d"%random.randint(1,30) 
    else:
        dzien = "%02d"%random.randint(1,31)
    
    plec = random.randint(0,9)

    roklist = list(str(rok)) 
    miesiaclist = list(str(miesiac))
    dzienlist = list(dzien)
    a = roklist[2]
    b = roklist[3]
    c = miesiaclist[0]
    d = miesiaclist[1]
    e = dzienlist[0]
    f = dzienlist[1]
    g = random.randint(0,9)
    h = random.randint(0,9)
    i = random.randint(0,9)
    j = plec
    k = random.randint(0,9)
    pesel = (a,b,c,d,e,f,g,h,i,j,k)
    lista = str(pesel)
    filepath = 'pesel.txt'
    f = open(filepath, "r+")
    f.write(lista)
    f.close()
generatepesel()