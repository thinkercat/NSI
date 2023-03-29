import csv

with open('sw.csv') as f:
    table = list(csv.DictReader(f,delimiter=','))

def search(value, table:list)->bool:
    '''
    Informe sur la présence de la valeur cherchée
    '''
    for e in table:
        for v in e.values():
            if v == value:
                return True

    return False

print(search('Dark Vador', table))