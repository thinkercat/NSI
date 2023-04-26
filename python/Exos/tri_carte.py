carte = [1,2,3,4,5,6,7,8,9,10,11,12,13]

def tri_selection(tab: list) -> None:
    n = len(tab)
    for i in range(n):
        indice_min = tab[0]
        for j in range( i, n):
            if tab[j] < tab[indice_min]:
                indice_min = j
        #il reste à échanger les valeurs d'indice i et indice_min
        tab[indice_min], tab[i] = tab[i], tab[indice_min]
    
    return tab
print(tri_selection([2,3,1]))
assert  tri_selection([2,3,1]) == [1,2,3]