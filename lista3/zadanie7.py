numbers = [0,1]
n = int(input())
print('')
def fibonacci(numbers):
    a = 0
    print(0)
    print(1)
    for i in range(n):
        a = numbers[-1] + numbers[-2]
        numbers.append(a)
        print(a)
fibonacci(numbers)
