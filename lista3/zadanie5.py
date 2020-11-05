import re
text = input()
x = re.search("[a-z]", text)
y = re.search("[A-Z]", text)
z = re.search("[0-9]", text)
c = re.search("[$#@]", text)
v = len(text)
if x:
    print('Hasło zawiera co najmniej 1 litere alfabetu[a−z]')
else:
    print('Hasło nie zawiera co najmniej 1 litery alfabetu[a−z]')
if y:
    print('Hasło zawiera co najmniej 1 literę alfabetu[A−Z]')
else:
    print('Hasło nie zawiera co najmniej 1 litery alfabetu[A−Z]')
if z:
    print('Hasło zawiera co najmniej 1 liczbę z przedziału [0-9]')
else:
    print('Hasło nie zawiera co najmniej 1 liczby z przedziału [0-9]')
if c:
    print('Hasło zawiera co najmniej 1 znak specjalny ze zbioru [$#@]')
else:
    print('Hasło nie zawiera co najmniej 1 znaku specjalnego ze zbioru [$#@]')
if v>=6 and v<=16:
    print('Hasło zawiera się w długości od 6 do 16 znaków')
else:
    print('hasło nie ma odpowiedniej długości')
