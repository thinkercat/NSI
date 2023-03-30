import csv

with open('sw.csv') as f:
    table = list(csv.DictReader(f,delimiter=','))

def search(value,filter:str, output:str ,table:list)->bool:
    '''
    Informe sur la présence de la valeur cherchée
    '''
    l = []
    for e in table:
        if e[filter] == value:
            l.append(e[output])

    return l

def count(value,filter:str, table):
    nb = 0
    for e in table:
        if e[filter] == value:
            nb += 1
    return nb

def values(value:str, filter:str, value2:str, filter2:str, table):
    return [e for e in table if e[filter] == value and e[filter2] == value2]

def projection(value:list, filter:list, table):
    r = []
    for i in range(len(value)):
        for e in table:
            if e[filter[i]] == value[i]:
                r.append(e)
    return r


#print( search('Sith', 'Statut', 'Nom', table))
#print( count('Sith', 'Statut', table))
#print( values('Sith', 'Statut','oui','Force', table))
#print(projection(['oui'], ['Force'], table))

def key(t):
    return (t['Espece'],t['Nom'])
    
table = sorted(table,key=key)

for e in table:
    print(e['Nom'])