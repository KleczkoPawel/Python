import time
print('Wprowadź liczbę wyrazów')
n = int(input())
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
start = time.time()
for i in range(n):
    print('wyraz numer ',i+1,' to: ',fibonacci(i))
print(time.time()-start)

