import time
print('Wprowadź liczbę wyrazów')
n = int(input())
def rekurencyjnie(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return rekurencyjnie(n-1)+rekurencyjnie(n-2)

def iteracyjnie(n):
    print('iteracyjnie \n')
    a,b=0,1
    start = time.time()
    print('wyraz 1: ',a)
    print('wyraz 2: ',b)
    for i in range(3,n+1):
        b,a=b+a,b
        print('wyraz',i,':',b)
    print(time.time()-start)

#  rekurencyjnie
print('rekurencyjnie \n')
start = time.time()
for i in range(n):
    print('wyraz numer ',i+1,' to: ',rekurencyjnie(i))
print(time.time()-start,'\n')

# iteracyjnie
iteracyjnie(n)

