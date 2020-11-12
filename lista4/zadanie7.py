def trojkat(n):
    a = []
    for x in range(n):
        a.append([])
        a[x].append(1)
        for z in range(1,x):
            a[x].append(a[x-1][z-1]+a[x-1][z])
        if (n!= 0):
            a[x].append(1)
    for x in range(n):
        print("    " * (n-x), end = "               ",)
        for z in range(0, x+1):
            print("{0:6}".format(a[x][z]), end = "  ",)
        print()
trojkat(8)