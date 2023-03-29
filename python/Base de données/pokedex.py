import csv

with open('pokedex.csv') as pokedex_data:
    table = list(csv.DictReader(pokedex_data,delimiter=';'))

def search(value, table:list)->bool:
    '''
    Informe sur la présence de la valeur cherchée
    '''
    for e in table:
        for v in e.values():
            if v == value:
                return True

    return False

print(search('Mew', table))