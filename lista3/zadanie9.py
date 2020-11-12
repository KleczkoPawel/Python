m = int(input())
n = int(input())
for i in range(1,m+1):
    tablica = ""
    for j in range(1,n+1):
        tablica = tablica +f'{i*j:5}'
    print(tablica)