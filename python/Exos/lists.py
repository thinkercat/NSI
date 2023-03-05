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
