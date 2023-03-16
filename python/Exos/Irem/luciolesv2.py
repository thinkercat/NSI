import imageio as imageio

image = imageio.imread('https://iremsinfo.callicode.fr/ressources/chal/LuciolesEnchantees2/plan_lucioles.png')

hauteur = image.shape[0]
largeur = image.shape[1]

def etat(h,l):
    R,V,B = image[h][l]
    if R == 255:
        return 1
    elif V == 255:
        return 2
    elif B == 255:
        return 3
    else:
        return 0

def voisines(h,l):
    voisines = []
    for y in range(h-8,h+8):
        for x in range(l-8,l+8):
            if y >= 0 and x >= 0 and y < hauteur and x < largeur:
                if etat(y,x) != 0:
                    voisines.append([y,x])
            
    return voisines


def createData(image):
    lucioles = {}
    for h in range(hauteur):
        for l in range(largeur):
            if image[h][l][0] != 0 or image[h][l][1] != 0 or image[h][l][2] != 0:
                lucioles[f"{h},{l}"] = {
                   "etat": etat(h,l),
                   "voisines" : voisines(h,l)
                }
    return lucioles

print(createData(image))

def updateEtat(data:dict):
    for pixel in data:
        somme_v = 0
        for voisine in pixel['voisines']:
            somme_v += etat(voisine[0],voisine[1])