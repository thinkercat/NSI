#### Les Fonctions ####
#def nom_de_ma_fonction():
    #actions de la fonction
#    print("ce que fais la fonction")
    #
    #
    #

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





def est_unicode(chainedecharactere:str):  
    ch_unicode = []
    for lettre in chainedecharactere:
        ch_unicode.append(ord(lettre.lower()))
        
    return ch_unicode # retourne une liste : 
Hello = [104,101,108,108,111]



def decale_lettres(liste:list,decalage:int):
    
    for lettre in range(len(liste)):
        liste[lettre] += decalage
        if liste[lettre] > 122:
            liste[lettre] -= 26
    return liste # retourne ma liste modifiée


def est_phrase(phrase_unicode:list):
    for lettre in range(len(phrase_unicode)):
        phrase_unicode[lettre] = chr(phrase_unicode[lettre])    
    return phrase_unicode


def decrypt(phrase_cryptée:str):
    
    phrase_cryptée_unicode = est_unicode(phrase_cryptée)
    solutions = []

    for decalage in range(1,26):
        print(decale_lettres(phrase_cryptée_unicode, decalage))
        solutions.append(decale_lettres(phrase_cryptée_unicode, decalage))
        print(solutions)


    for solution in range(len(solutions)):
        solutions[solution] = est_phrase(solutions[solution])
    
    return solutions


def test_decrypt():
    assert est_unicode("Hello") == [104,101,108,108,111]
    assert est_unicode("abcde") == [97,98,99,100,101]
    print("Fonction est_unicode()....OK")

    assert decale_lettres([104,101,108,108,111],1) == [105,102,109,109,112]
    assert decale_lettres([104,101,108,108,111],5) == [109,106,113,113,116]
    assert decale_lettres([121,122],2) == [97,98]
    print("Fonction decale_lettre()....OK")

    assert est_phrase([104,101,108,108,111]) == ['h','e','l','l','o']
    assert est_phrase([97,98,99,100,101]) == ['a','b','c','d','e']
    print("Fonction est_phrase()....OK")

test_decrypt()

print(decrypt("Gdkkn"))