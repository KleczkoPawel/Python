def suma(n):
    an = 1/n
    b = []
    for x in range(1, n+1, 1):
        x = 1/x
        b.append(x)
        c = sum(b)
    print(c)
suma(4)