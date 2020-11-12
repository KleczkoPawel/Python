def euklides(a,b):
    while b!= 0:
        mod = a%b
        a = b
        b = mod
    print(a)
euklides(4,400)