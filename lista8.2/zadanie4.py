import os
import sys
def sprawdz():
    filepath = 'pesel.txt'
    f = open(filepath, "r+")                        # poprawić na sprawdzanie 10 peseli na raz
    peselzip = f.read()
    a = list(peselzip)
    c=""
    rok = ""
    
    for i in a:
        if i.isnumeric():
            c = c + i

    miesiac = c[2]+c[3]
    dzien = c[4]+c[5]
    
    if int(miesiac)>12:
        miesiac = int(miesiac) - 20
        r1 = 20
        miesiacstr = str(miesiac)
        if len(miesiacstr)==1:
            miesiac = '0'+str(miesiac)
    else:
        miesiac = miesiac
        r1 = 19

    if len(dzien)==1:
        dzien = '0'+dzien

    roklista = [str(r1)+c[0]+c[1]]

    for i in roklista:
        rok += i
                            ### Sprawdzenie roku przestępnego ###
    if int(rok) % 4 == 0:
        if miesiac == '02':
            if int(dzien)>28:
                print('Pesel jest niepoprawny')
                                    ### Sprawdzenie płci ###
    if int(c[9])%2 == 0:
        plec = 'Kobieta'
    else:
        plec = 'Mężczyzna'

    if int(dzien)>31:
        print('Pesel jest niepoprawny')

    if (1*int(c[0]) + 3*int(c[1]) + 7*int(c[2]) + 9*int(c[3]) + 1*int(c[4]) + 3*int(c[5]) + 7*int(c[6]) + 9*int(c[7]) + 1*int(c[8]) + 3*int(c[9]) + 1*int(c[10]))%10 == 0:
        print('Pesel jest poprawny')
        print('Data urodzenia: '+rok+'-'+miesiac+'-'+dzien+'\n Płeć : '+plec)
    else:
        print('Pesel jest niepoprawny')

    print(c)

    f.write("rok : " + rok +" ;miesiac : "+str(miesiac) + ";dzien : " + dzien + ";plec : " + plec)
    os.rename(filepath,'nr'+c+'/%' + dzien + "-%" + str(miesiac) + "-%" + dzien +";/%"+plec)
    f.close()

sprawdz()
    