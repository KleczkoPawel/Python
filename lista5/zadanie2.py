a = int(input())
def zmiana(kod):
    jednosci = {'0':"",'1':"jeden",'2':"dwa",'3':"trzy",'4':"cztery",'5':"pięć",'6':"sześć",'7':"siedem",'8':"osiem",'9':"dziewięć"}
    nascie = {'0':"",'10':"dziesięć",'11':"jedenaście",'12':"dwanaście",'13':"trzynaście",'14':"czternaście",'15':"piętnaśćie",'16':"szesnaście",'17':"siedemnaście",'18':"osiemnaście",'19':"dziewiętnaście"}
    dziesiatki = {'0':"",'2':"dwadzieścia",'3':"trzydzieści",'4':"czterdzieści",'5':"pięćdziesiąt",'6':"sześćdziesiąt",'7':"siedemdziesiąt",'8':"osiemdziesiąt",'9':"dziewięćdziesiąt"}
    setki = {'0':"",'1':"sto",'2':"dwieście",'3':"trzysta",'4':"czterysta",'5':"pięćset",'6':"sześćset",'7':"siedemset",'8':"osiemset",'9':"dziewięćset"}
    tysiac = {'1':"tysiąc"}
    astr = str(a)
    if len(astr)==1:
        print(jednosci[astr])
    if len(astr)==2:
        if a<20:
            print(nascie[astr])
        if a>19:
            print(dziesiatki[astr[0]],jednosci[astr[1]])
    if len(astr)==3:
        print(setki[astr[0]],dziesiatki[astr[1]],jednosci[astr[2]])
    if len(astr)==4:
        print(tysiac[astr[0]],setki[astr[1]],dziesiatki[astr[2]],jednosci[astr[3]])
zmiana(a)