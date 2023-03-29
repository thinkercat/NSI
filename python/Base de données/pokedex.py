import csv

with open('pokedex.csv') as pokedex_data:
    table = list(csv.DictReader(pokedex_data,delimiter=';'))

print(table[0]['code'])