#! py
import matplotlib.pyplot as plt

def syracuse(n:int):
    '''
    Effectue la conjecture de syracuse
    '''
    suite_n = []
    suite_n.append(n)
    while n != 1 :
        
        if n % 2 == 0:
            n = n // 2
        
        else:
            n = n*3
            n +=1
        suite_n.append(n)
    return suite_n

def svnt_syracuse(n:int):
    if n % 2 == 0:
        n = n // 2
    else:
        n = n * 3
        n += 1
    return n

def tempsvol(n:int) -> int:
    return len(syracuse(n))

def tempsvol_alt(n:int) -> int:
    '''
    renvoie le nombre d'itérations superieur à n dans la suite de syracuse de n
    '''
    iter = 0
    for v in syracuse(n):
        if v >= n:
            iter += 1
    return iter

def alt_max(n:int) -> int:
    return max(syracuse(n))

def affiche_syracuse(n:int) -> None:
    '''
    affiche la syracuse de n
    '''
    # Paramètres de la fenetre
    plt.title('Syracuse de '+str(n))
    plt.xlabel('temps de vol')
    plt.ylabel('hauteur de vol')

    x = range(0,len(syracuse(n)))
    y = syracuse(n)
    
    plt.plot(x , y, 'o-r')

    plt.show()
    
n = int(input("Entrez un nombre :"))
affiche_syracuse(n)