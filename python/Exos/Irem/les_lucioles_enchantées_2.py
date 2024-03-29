import imageio as imageio
import numpy

image = imageio.imread('https://iremsinfo.callicode.fr/ressources/chal/LuciolesEnchantees2/plan_lucioles.png')

hauteur = image.shape[0]
largeur = image.shape[1]


#print(type(image))
def voisines(h,l):
    voisines = []
    for y in range(hauteur//8):
        for x in range(largeur//8):

            if abs(h-y) <= 8 and abs(l-x) <= 8:
                voisines.append([y,x])

    return voisines

def pixelcolor(h,l):
    R,V,B = image[h,l]
    if R == 255:
        return 'red'
    elif V == 255:
        return 'vert'
    elif B == 255:
        return 'bleu'

def etat(h,l):
    if pixelcolor(h,l) == 'rouge':
        return 1
    elif pixelcolor(h,l) == 'vert':
        return 2
    elif pixelcolor(h,l) == 'bleu':
        return 3
    else:
        return 0

for t in range(1000):
    for h in range(hauteur):
        for l in range(largeur):

            pos_voisines = []
            if image[h][l][0] != 0 or image[h][l][1] != 0 or image[h][l][2] != 0:
                # print(f'\n color : {image[h][l]}')
                
                pos_voisines = voisines(h,l)
                somme_etats = 0
                for v in pos_voisines:
                    # print(v)
                    # print(image[v[0]][v[1]])
                    # print(type(etat(v[0],v[1])))
                    somme_etats += int(etat(v[0],v[1]))

                if somme_etats >= 5:
                    if etat(h,l) == 1:
                        image[h][l] = [0,255,0]

                    elif etat(h,l) == 2:
                        image[h][l] = [0,0,255]

                    elif etat(h,l) == 3:
                        image[h][l] = [255,0,0]

                else:
                    if etat(h,l) == 1:
                        image[h][l] = [0,0,255]

                    elif etat(h,l) == 2:
                        image[h][l] = [255,0,0]

                    elif etat(h,l) == 3:
                        image[h][l] = [0,255,0]
            # else:
            #     # print(f"color : {image[h][l]}")
    print(t)

imageio.imsave(f'lucioles.png', image)

print("End")