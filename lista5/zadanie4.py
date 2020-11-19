litery = {"a" : "y", "e" : "i", "i" : "o", "o" : "a", "y" : "e","b":"b", "c":"c", "d":"d", "f":"f", "g":"g","h":"h", "j":"j","k":"k","l":"l","m":"m","n":"n","u":"u","p":"p","r":"r","s":"s","t":"t","w":"w","v":"v","x":"x","z":"z"," ":" "}
print('Wprowadz tekst do zaszyfrowania :')
a = input()
def szyfrowanie(tekst):
    print('Tekst po zaszyfrowaniu :')
    for litera in tekst:
        print(litery[litera],end='')
szyfrowanie(a)

print('\n','Tekst po deszyfrowaniu :')
def deszyfrowanie(tekst):
    for litera in tekst:
        print(litera,end='')
deszyfrowanie(a)