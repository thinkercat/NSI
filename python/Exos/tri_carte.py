import time
import random as rd
import matplotlib.pyplot as plt

carte = [1,2,3,4,5,6,7,8,9,10,11,12,13]

def tri_selection(tab: list):
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

def tri_insertion(tab:list):
    """
    Tri par selection
    """
    for i in range(1,len(tab)):
        v = tab[i]
        j = i - 1

        while tab[j] > v and j >= 0:
            tab[j+1] = tab[j]
            j-=1

        tab[j+1] = v
    return tab

assert  tri_insertion([2,3,1]) == [1,2,3]
assert  tri_insertion([2,3,1,15,17,12]) == [1,2,3,12,15,17]

def tri_parallele(tab:list):
    """
    Tri en parallele pour des listes à valeur double
    """
    i = 0
    j = len(tab)-1
    v_min = min(tab)
    while i != j:
        if tab[i] > v_min:
            tab[i], tab[j] = tab[j], tab[i]
            j -= 1
        else:
            i += 1
    return tab

assert tri_parallele([1,1,0,1,0,0]) == [0,0,0,1,1,1]
assert tri_parallele([2,6,2,2,6,2,2,6,6,2,2]) == [2,2,2,2,2,2,2,6,6,6,6]


def alea(n):
    lst_alea = list(range(n))
    rd.shuffle(lst_alea)
    return lst_alea

def chrono_ins(n):
    t0 = time.time()
    tri_insertion(n)
    t1 = time.time()
    return t1-t0

def chrono_sel(n):
    t0 = time.time()
    tri_selection(n)
    t1 = time.time()
    return t1-t0

tailles = [10, 50, 100, 500, 1000, 2000, 5000, 10000]
temps_ins = [chrono_ins(alea(k)) for k in tailles]
temps_sel = [chrono_sel(alea(k)) for k in tailles]

# plt.plot(tailles, temps_ins,tailles, temps_sel)
# plt.show()
