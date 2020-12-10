import time
print('Wprowadź liczbę wyrazów')
n = int(input())
def fibonacci(n):
    a = 0
    b = 1
    start = time.time()
    print('wyraz 1: ',a)
    print('wyraz 2: ',b)
    for i in range(3,n):
        b=b+a
        a=b-a
        print('wyraz',i,':',b)
    print(time.time()-start)
fibonacci(n)