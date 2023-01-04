
tab = [list(row) for row in open('python/Exos/input.txt').read().splitlines()]

tableau = 0
for l in tab:
    tableau +=1
    charCount = 0
    for letter in l:
        charCount +=1
        if ord(letter) <= 90:
            print(f'{tableau}:{charCount}')
            