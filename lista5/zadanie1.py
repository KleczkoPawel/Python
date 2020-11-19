a = input()
b = a.split()
def zmiana(kod):
    jednosci = {'0':"",1:"jeden",2:"dwa",'3':"trzy",'4':"cztery",'5':"pięć",'6':"sześć",'7':"siedem",'8':"osiem",'9':"dziewięć",'10':"dziesięć",'11':"jedenaście",'12':"dwanaście",'13':"trzynaście",'14':"czternaście",'15':"piętnaśćie",'16':"szesnaście",'17':"siedemnaście",'18':"osiemnaście",'19':"dziewiętnaście"}
    dziesiatki = {'0':"",20:"dwadzieścia",'3':"trzydzieści",'4':"czterdzieści",'5':"pięćdziesiąt",'6':"sześćdziesiąt",'7':"siedemdziesiąt",'8':"osiemdziesiąt",'9':"dziewięćdziesiąt"}
    reversed_jednosci = {value : key for (key, value) in jednosci.items()}
    reversed_dziesiatki = {value : key for (key, value) in dziesiatki.items()}
    if len(b)==1:
        print(reversed_jednosci[a])
    if len(b)==2:
        print((reversed_dziesiatki[b[0]])+(reversed_jednosci[b[1]]))
zmiana(a)