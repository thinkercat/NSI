dico = {}
dico = dict()
chiffres = ['zéro', 'un', 'deux', 'trois', 'quatre', 'cinq', 'six', 'sept', 'huit', 'neuf']
for c in chiffres:
    dico[c] = len(c)

def getKeys(dico:dict,v)->list:
    return [k for k in dico if dico[k] == v]

assert getKeys(dico,4) == ['zéro','deux','cinq','sept','huit','neuf']



habits = {"pantalons": 3, "pulls": 4, "tee-shirts": 8}

def newClothe(name, number):
    try:
        habits[name] += number
    except KeyError:
        habits[name] = number

newClothe('robe', 2)
newClothe('chemise', 5)
#print(habits)

lst = ['5717', '1133', '5545', '4031', '6398', '2734', '3070', '1346', '7849', '7288', '7587', '6217', '8240', '5733', '6466', '7972', '7341', '6616', '5061', '2441', '2571', '4496', '4831', '5395', '8584', '3033', '6266', '2452', '6909', '3021', '5404', '3799', '5053', '8096', '2488', '8519', '6896', '7300', '5914', '7464', '5068', '1386', '9898', '8313', '1072', '1441', '7333', '5691', '6987', '5255']

def mostInList(list:list=lst)->int:
    numbers = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
    for e in lst:
        for chiffre in e:
            numbers[chiffre] += 1

    #print(numbers)
    nMax = 0
    numberMax = 0
    for n in numbers:
        if numbers[n] > nMax:
            nMax = numbers[n]
            numberMax = n
    # ou
    nMax = 0
    numberMax = 0
    for key, value in numbers.items():
        if value > nMax:
            nMax = value
            numberMax = key
    
    return numberMax
print(mostInList(lst))

exemple_pokemons = {
    'Bulbizarre': (70, 7),
    'Herbizarre': (100, 13),
    'Abo': (200, 7),
    'Jungko': (170, 52),
    'Canartichaud' : (160,15),
    'Dracaufeu' : (230,300)
    }
def plus_grand(pokemons: dict) -> tuple:
    nom_plus_grand = ''
    taille_max = 0
    for v in pokemons :
        if  pokemons[v][0] > taille_max:
            nom_plus_grand = v
            taille_max = pokemons[v][0]
    
    # or
    t_max = 0
    name = ''
    for key,v in pokemons.items():
        if v[0] > t_max:
            t_max = v[0]
            name = key
    
    
    return name, t_max

print(plus_grand(exemple_pokemons))

dico_gen = {
    'UUU': 'F', 'UUC': 'F', 'UUG': 'L', 'UUA': 'L', 'UCU': 'S',
    'UCC': 'S', 'UCG': 'S', 'UCA': 'S', 'UAU': 'Y', 'UAC': 'Y',
    'UAG': 'X', 'UAA': 'X', 'UGU': 'C', 'UGC': 'C', 'UGG': 'W',
    'UGA': 'X', 'CUU': 'L', 'CUC': 'L', 'CUG': 'L', 'CUA': 'L',
    'CCU': 'P', 'CCC': 'P', 'CCG': 'P', 'CCA': 'P', 'CGU': 'R',
    'CGC': 'R', 'CGG': 'R', 'CGA': 'R', 'CAU': 'H', 'CAC': 'H',
    'CAG': 'Q', 'CAA': 'Q', 'ACU': 'T', 'ACC': 'T', 'ACG': 'T',
    'ACA': 'T', 'AUG': 'M', 'AUU': 'I', 'AUC': 'I', 'AUA': 'I',
    'AAU': 'N', 'AAC': 'N', 'AAG': 'K', 'AAA': 'K', 'AGU': 'S',
    'AGC': 'S', 'AGG': 'R', 'AGA': 'R', 'GUU': 'V', 'GUC': 'V',
    'GUG': 'V', 'GUA': 'V', 'GCU': 'A', 'GCC': 'A', 'GCG': 'A',
    'GCA': 'A', 'GGU': 'G', 'GGC': 'G', 'GGG': 'G', 'GGA': 'G',
    'GAU': 'D', 'GAC': 'D', 'GAG': 'E', 'GAA': 'E'
    }

def traduction(texte:str,dico_gen=dico_gen): 
    return ''.join([dico_gen[texte[l:l+3]] for l in range(0,len(texte),3)])

print(traduction('CAUAUA'))

def jour_suivant(date:tuple):
    jours = ["dimanche", "lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi"]

    mois = [
        "janvier", "février", "mars", "avril",
        "mai", "juin", "juillet", "aout",
        "septembre", "octobre", "novembre", "décembre",
    ]

    duree_mois = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    nom_jour = date[0]
    indice_jour_suivant = (jours.index(nom_jour) + 1) % 7
    numero_mois = date[2]
    x = 2
    numero_mois_suivant = (numero_mois + x) %12
    return (jours[(jours.index(date[0])+1)%7], numero_mois_suivant)
print(jour_suivant(("samedi", 21, 10, 1995)))