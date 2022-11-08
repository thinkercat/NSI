#### Les Fonctions ####
#def nom_de_ma_fonction():
    #actions de la fonction
#    print("ce que fais la fonction")
    #
    #
    #

from random import randint


def sommes_entiers(valeur:int=300):
    s = 0 
    for k in range(1, valeur+1):
        s += k
    
    return(s)

print(sommes_entiers(42))

def tirage():
    tirage = randint(1,18)
    if tirage >= 6:
        return(6)
    else:
        return(tirage)
