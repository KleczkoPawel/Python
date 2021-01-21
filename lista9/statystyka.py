import numpy as np
def statystyka(dane):
    dane = open(dane,"r")
    lista = dane.read()
    listadanych = list(lista)
    suma = 0
    argumenty = 0
    for d in dane:
        if d.isnumeric()==True:
            suma += d
            argumenty += 1

    srednia = "{:.2f}".format(suma/argumenty)
    wariacja =  "{:.2f}".format(np.var(dane))
    odchylenie =  "{:.2f}".format(np.std(dane))

    print('srednia : '+srednia+'\n'+
          'wariacja : '+wariacja+'\n'+
          'odchylenie : '+odchylenie)
        
statystyka('dane.txt')
