import itertools
def permutation(lista):
    a = itertools.permutations(lista)
    b = list(a)
    print(b)
permutation(lista=[1,2,3,4])
