import random
import time

zbior = []
for i in range(300):
    zbior.append(random.randint(0, 20))

start = time.time()
def sortprzezwstawianie(zbior):
    length = len(zbior)
    
    for i in range(1, length):
        obecny = zbior[i]
        j = i-1
        while j >= 0 and obecny < zbior[j]:
            zbior[j+1] = zbior[j]
            j -= 1
        zbior[j+1] = obecny
    return zbior

print(sortprzezwstawianie(zbior))
print(time.time()-start)
# dla 300 ~~ 0.0034s
# dla 200 ~~ 0.0018s
# dla 100 ~~ 0.0005s