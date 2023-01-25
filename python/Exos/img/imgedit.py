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
    cimage = image.copy()
    for y in range(hauteur//2):
        for x in range(largeur//2):
            pass     

    return image
            




#linux
#image = imageio.imread('/home/nsi/Documents/NSI/VanGogh_Arles.png')
#image = imageio.imread('/home/nsi/Documents/NSI/carrescolor.png')
#windows
image = imageio.imread('NSI\\VanGogh_Arles.png')
#image = imageio.imread('NSI\\carrescolor.png')
hauteur = image.shape[0]
largeur = image.shape[1]
print(f'{hauteur}:{largeur}')


# for y in range(hauteur):
#     for x in range(largeur):
#         R,G,B = image[y][x]
#         #image[y][x] = gris(R,G,B)

imageio.imsave('imagemodifie.png', photomaton(image))