import string
def szyfr(tekst,n):
    for litera in tekst:
        if litera in string.ascii_lowercase:
            b = ord(litera)
            if b <= 122-n:
                c = chr(b+n)
            else:
                c = chr(b+n-26)
        elif litera in string.ascii_uppercase:
            b = ord(litera)
            if b <= 90-n:
                c = chr(b+n)
            else:
                c = chr(b+n-26)
        else:
                c = litera
    return c
def deszyfr(tekst,n):
    for litera in tekst:
        if litera in string.ascii_lowercase:
            b = ord(litera)
            if b-n < 97:
                c = chr(b-n+26)
            else:
                c = chr(b-n)
        elif litera in string.ascii_uppercase:
            b = ord(litera)
            if b-n < 65:
                print(n)
                c = chr(b-n+26)
            else:
                c = chr(b-n)
        else:
            c = litera
    return c
