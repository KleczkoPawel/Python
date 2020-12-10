import random
import time

zbior = []
for i in range(100):
    zbior.append(random.randint(0, 20))

start = time.time()
def sortbabelkowe(zbior):
    length = len(zbior)
    while length > 1:    
        for i in range(0, length-1):
            if zbior[i] > zbior[i+1]:
                zbior[i], zbior[i+1] = zbior[i+1], zbior[i]
        length -= 1
    return zbior

print(sortbabelkowe(zbior))
print(time.time()-start)
# dla 300 ~~ 0.007s
# dla 200 ~~ 0.004s
# dla 100 ~~ 0.001s