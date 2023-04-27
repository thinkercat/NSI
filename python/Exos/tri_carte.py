import time
import random as rd
import matplotlib.pyplot as plt

carte = [1,2,3,4,5,6,7,8,9,10,11,12,13]

def tri_selection(tab: list) -> None:
    n = len(tab)
    for i in range(n):
        indice_min = i

        for j in range(i, n):
            if tab[j] < tab[indice_min]:
                indice_min = j

        tab[indice_min], tab[i] = tab[i], tab[indice_min]
    return tab

assert  tri_selection([2,3,1]) == [1,2,3]
assert  tri_selection([2,3,1,15,17,12]) == [1,2,3,12,15,17]



def alea(n):
    lst_alea = list(range(n))
    rd.shuffle(lst_alea)
    return lst_alea

def chrono(n):
    t0 = time.time()
    tri_selection(n)
    t1 = time.time()
    return t1-t0

tailles = [10, 50, 100, 500, 1000, 2000, 5000, 10000]
temps = [chrono(alea(k)) for k in tailles]


plt.plot(tailles, temps)
plt.show()
