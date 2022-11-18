

from random import randint

def sommes_entiers(valeur:int):
    s = 0 
    for k in range(1, valeur+1):
        s += k
    
    return s

def comptevoyelles(phrase:str):
    voyelles = 'aeiouy'
    nb_voyelles = 0
    for lettre in phrase:
        if lettre in voyelles:
            nb_voyelles += 1
    return nb_voyelles

def test_nb_voyelles():
    assert comptevoyelles("azerty") == 3
    assert comptevoyelles("pglmj") == 0
    assert comptevoyelles("aeiouy") == 6

    print("..... Test OK")
    return True


def tirage():
    tirage = randint(1,18)
    if tirage >= 6:
        return(6)
    else:
        return tirage


def minmax(nombre01:int,nombre02:int):
    if nombre01 > nombre02:
        return nombre01
    else:
        return nombre02



############# TP Cryptographie #################

# Première remarque : c'est très bien de préciser le type 
# de retour de la fonction, et de mettre un exemple.
# On peut "normaliser" cette pratique, lis le cours sur la
# spécification des fonctions. Cela donnerait quelque chose
# comme ça:

def est_unicode(chainedecharactere:str) -> list: 
    '''
    renvoie la liste composée des codes Unicode des caractères
    de la chaîne en paramètre.
    Exemple:
    >>> est_unicode('Hello')
    [104,101,108,108,111]
    '''
    ch_unicode = []
    for lettre in chainedecharactere:
        ch_unicode.append(ord(lettre.lower()))
        
    return ch_unicode  

def decale_lettres(liste_unicode:list, decalage:int):
    liste = []
    i = 0
    for lettre in liste_unicode:
        i += 1
        liste.append(lettre + 1)
        if liste[i] > 122:
            liste[i] -= 26
    return liste # retourne ma liste modifiée

'''
Le problème se situe dans la fonction suivante (mais aussi
dans la précédente, sans conséquence.
C'est une histoire de modification en dehors de la fonction
(un effet de bord).
En fait, comme ton paramètre est une liste, les modifications
que tu lui apportes dans ta fonction vont affecter la liste
passée en paramètre.
Et donc après le premier appel, la liste phrase_unicode comporte
des caractères et non plus des entiers.
D'où l'erreur.

Exemple, teste:

lst = [1, 2, 3]
def decale_un(l):
    for k in range(len(l)):
        l[k] += 1
    return l

lst2 = decale_un(lst)
print(lst2)
print(lst)

Tu comprends ce qui se passe?

Pour remédier au problème, construis une **nouvelle** liste
dans ta fonction est_phrase sans toucher à ta liste en 
paramètre, puis renvoie cette nouvelle liste.
'''

def est_phrase(phrase_unicode:list):
    est_phrase = []
    for lettre in range(len(phrase_unicode)):
        est_phrase.append(chr(phrase_unicode[lettre]))

    return est_phrase

def unlist(liste_characteres:list) -> str:
    '''
    Transforme une liste de characteres en string
    Ex: ['N','A','S','A'] -> NASA
    '''
    chaine_str = ''
    for lettre in liste_characteres:
        chaine_str += lettre
    
    return chaine_str


def decrypt(phrase_cryptée:str):

    phrase_cryptée_unicode = est_unicode(phrase_cryptée)    

    for decalage in range(1,25):

      
        print(unlist(est_phrase(decale_lettres(phrase_cryptée_unicode, decalage))))




def test_decrypt():
    assert est_unicode("Hello") == [104,101,108,108,111]
    assert est_unicode("abcde") == [97,98,99,100,101]
    print("Fonction est_unicode()....OK")

    # assert decale_lettres([104,101,108,108,111],1) == [105,102,109,109,112]
    # assert decale_lettres([104,101,108,108,111],5) == [109,106,113,113,116]
    # assert decale_lettres([121,122],2) == [97,98]
    print("Fonction decale_lettre()....OK")

    assert est_phrase([104,101,108,108,111]) == ['h','e','l','l','o']
    assert est_phrase([97,98,99,100,101]) == ['a','b','c','d','e']
    print("Fonction est_phrase()....OK")

    assert unlist(['N','A','S','A']) == "NASA"
    assert unlist(["H","e","l","l","o","W","o","r","l","d"]) == "HelloWorld"
    print("Fonction unlist()....OK")
test_decrypt()

print(decrypt("abcde")) # hello decalage 2
# PRZRFFNTRARPBAGVRAGEVRAQVAGRERFFNAGZNVFVYRFGFHSSVFNZZRAGYBATCBHEARCNFYRQRPELCGRENYNZNVA