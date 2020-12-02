import string
def szyfr(tekst):
    for litera in tekst:
        if litera in string.ascii_letters:
            b = ord(litera)
            if b < 109:
                c = chr(b+13)
            else:
                c = chr(b+13-25)
            print(c,end='')
        elif litera in string.ascii_uppercase:
            b = ord(litera)
            if b < 77:
                c = chr(b+13)
            else:
                c = chr(b+13-25)
            print(c,end='')
        else:
            print(litera,end='')
def deszyfr(tekst):
       for litera in tekst:
        if litera in string.ascii_letters:
            b = ord(litera)
            if b > 109:
                c = chr(b-13)
            else:
                c = chr(b-13+25)
            print(c,end='')
        elif litera in string.ascii_uppercase:
            b = ord(litera)
            if b > 77:
                c = chr(b-13)
            else:
                c = chr(b-13+25)
            print(c,end='')
        else:
            print(litera,end='')