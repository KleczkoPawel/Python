print('Wprowadz liczbę rzymską')
a = input()
def zmiana(kod):
    jeden = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    dwa = {'II':2,'IV':4,'VI':6,'IX':9,'XI':11,'XV':15,'XX':20,'XL':40,'LI':51,'LV':55,'LX':60,'XC':90,'CC':200,'CD':400,'DC':600,'MM':2000}
    if len(a)==1:
        print(jeden[a])
    if len(a)==2:
        print(dwa[a])
    if len(a)==3:
        print((jeden[a[0]])+(dwa[a[1:]]))
    if len(a)==4:
        print((jeden[a[0]])+(jeden[a[1]])+(dwa[a[2:]]))
print('Postac dziesietna wprowadzonej liczby to :')
zmiana(a)