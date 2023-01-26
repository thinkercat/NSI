#import imageio
import imageio.v2 as imageio
def filtre(R:int,G:int,B:int, color = 'rouge')->list:
    '''
    Affiche l'image avec un filtre de couleur rouge, vert ou bleu
    '''
    if color == 'rouge':
        return [R,0,0]
    elif color == 'vert':
        return [0,G,0]
    elif color == 'bleu':
        return [0,0,B]

def negatif(R:int,G:int,B:int)->list:
    '''
    Renvoie les pixels en négatifs
    '''
    return [255-R,255-G,255-B]

def gris(R:int,G:int,B:int):
    '''
    Renvoie les pixels en niveaux de gris
    '''
    G = int(0.2126*R+0.7152*G+0.0722*B)
    return [G,G,G]

def popart(R:int,G:int,B:int)->list:
    '''
    Renvoie la valeure majoritaire + 50
    '''
    color = [R,G,B]

    if max(color) + 50 < 255:
        color = [int(str(c).replace(str(max(color)),'255')) for c in color]
    else:
        color = [int(str(c).replace(str(max(color)),str(max(color)+50))) for c in color]
    return color
def flopart(R:int,G:int,B:int)->list:
    '''
    Renvoie la valeure majoritaire + 50
    '''
    color = [R,G,B]

    if max(color) - 50 < 0:
        color = [int(str(c).replace(str(max(color)),'0')) for c in color]
    else:
        color = [int(str(c).replace(str(max(color)),str(max(color)-50))) for c in color]
    return color
def flip(image):
    hauteur = image.shape[0]
    largeur = image.shape[1]
    imagecopy = image.copy()
    for y in range(hauteur):
        for x in range(largeur):
            if x < largeur//2:
                image[y][x] = image[y][largeur-x-1]
            else:
                image[y][x] = imagecopy[y][largeur-x-1]
    return image

def photomaton(image):
        
    hauteur = image.shape[0]
    largeur = image.shape[1]
    image_p = []
    ypair = []
    yimpair = []
    for y in range(hauteur):
        if y%2 == 0:
            ypair.append(image[y])
        else:
            yimpair.append(image[y])
    image_p = ypair + yimpair

    for y in range(hauteur):
        xpair = []
        ximpair = []
        for x in range(largeur):
            if x%2 == 0:
                xpair.append(image[y][x])
            else:
                ximpair.append(image[y][x])
        image[y] = xpair + ximpair
    return image_p

def pixelisation(etendue = 1):
    pass       




#linux
#image = imageio.imread('/home/nsi/Documents/NSI/VanGogh_Arles.png')
#image = imageio.imread('/home/nsi/Documents/NSI/carrescolor.png')
#windows
image = imageio.imread('NSI\\VanGogh_Arles.png')
#image = imageio.imread('NSI\\carrescolor.png')
hauteur = image.shape[0]
largeur = image.shape[1]
print(f'{hauteur}:{largeur}')


for y in range(hauteur):
    for x in range(largeur):
        R,G,B = image[y][x]
        image[y][x] = flopart(R,G,B)

imageio.imsave('imagemodifie.png', image)