def recherche(tab:list,n):
    
    occ = len(tab)
    i = 0

    for v in tab:
    
        if v == n:
            occ = i
        i += 1
    
    return occ

#print(recherche([1,2,3,4],2))
#print(recherche([1,3,4],2))
#print(recherche([1,2,3,4,2],2))

# for bb in range(1,1001):
#     for br in range(bb,1001):
#         for bn in range(br,(bb*2)):
#             if (bb+br+bn)*777 == bb*br*bn:
#                 print(bb,br,bn)
#                 print(bb+br+bn)
#                 quit()

def test(h):
    return h

l = [1,2]

f = [1,2]

if l == [1,2]:
    print('work')

def ajoute_dictionnaires(d1:dict,d2:dict)->dict:
    """
    Fusionne deux dictionnaires de types {int:int}
    """
    d = {}
    #keys = set(d1.keys()) | set(d2.keys())
    keys = [k for k in d1.keys()] + [k for k in d2.keys()]

    for key in keys:
        if key in d1 and key in d2:
            d[key] = d1[key] + d2[key] 
        elif key in d1:
            d[key] = d1[key] 
        else:
            d[key] = d2[key]

    return d

assert ajoute_dictionnaires({1: 5, 2: 7}, {2: 9, 3: 11}) == {1: 5, 2: 16, 3: 11}
assert ajoute_dictionnaires({}, {2: 9, 3: 11}) == {2: 9, 3: 11}
assert ajoute_dictionnaires({1: 5, 2: 7}, {}) == {1: 5, 2: 7}