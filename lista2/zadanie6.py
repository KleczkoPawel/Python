lista = ['Kasia','Basia','Marek','Darek']

lista.append ('Józek')

kobity = ['Ania','Basia']

lista.extend (kobity)

lista.sort()

print (lista)

print (lista[3]) # czwarty student na liście:

print (lista[0:2]) # dwaj pierwsi na liście:

print (lista[5:7]) # dwaj ostatni na liście:

lista = list (dict.fromkeys(lista))

lista.remove ('Basia')

print (lista) 

print (len(lista)) # liczba studentów

tuple1 = tuple(lista)

print (tuple1)




