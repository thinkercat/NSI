# Eliott LAURE-GERMAIN
# Mini projet : image

#----------IMPORTS-----------#
import os
import sys
from math import *
import imageio
#import imageio.v2 as imageio


#--------------CODES--------------#
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

#-

def negatif(R:int,G:int,B:int)->list:
    '''
    Renvoie les pixels en négatifs
    '''
    return [255-R,255-G,255-B]

#-

def gris(R:int,G:int,B:int):
    '''
    Renvoie les pixels en niveaux de gris
    '''
    G = int(0.2126*R+0.7152*G+0.0722*B)
    return [G,G,G]

#-

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

#-

def flopart(R:int,G:int,B:int)->list:
    '''
    Renvoie la valeure majoritaire - 50
    '''
    color = [R,G,B]

    if max(color) - 50 < 0:
        color = [int(str(c).replace(str(max(color)),'0')) for c in color]
    else:
        color = [int(str(c).replace(str(max(color)),str(max(color)-50))) for c in color]
    return color

#-

def flip(image:list)->list:
    '''
    Inverse le sens de l'image
    '''
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

#-

def photomaton(image:list)->list:
    '''
    Divise l'image en 4 images
    '''
    hauteur = image.shape[0]
    largeur = image.shape[1]
    cimage = image.copy()
    for y in range(hauteur):
        for x in range(largeur):
                if y%2 == 0:
                    if x%2 == 0:
                        cimage[y//2 + hauteur//2][x//2 + largeur//2] = image[y][x]
                    else:
                        cimage[y//2 + hauteur//2][x//2] = image[y][x]
                elif x%2 == 0:
                    cimage[y//2][x//2 + largeur//2] = image[y][x]
                else:
                    cimage[y//2][x//2] = image[y][x]

    return cimage

#-

def pixelisation(image,etendue = 6):
    '''
    Pixelise l'image (l'étendue de pixelisation peut varier)
    '''
    hauteur = image.shape[0]
    largeur = image.shape[1]

    if etendue > largeur:
        etendue = largeur
        
    if 256%etendue != 0:
        while 256%etendue != 0:
            etendue += 1
    
    Un = 1
    for n in range(etendue):
        Un = (sqrt(Un)+2)**2
    nb_pixel = Un
    hauteur = image.shape[0]
    largeur = image.shape[1]
    cimage = image.copy()

    for cy in range(hauteur//etendue):
        for cx in range(largeur//etendue):

            cmoy = [0,0,0]
            for v in range(etendue):
                for w in range(etendue):

                    for c in range(3):
                        cmoy[c] += image[cy*etendue+v][cx*etendue+w][c] // (etendue**2)

            for y in range(etendue):
                for x in range(etendue):

                    cimage[cy*etendue+y][cx*etendue+x] = cmoy
    return cimage

#-

def flou(image,etendue = 3):
    '''
    Floute l'Image
    '''   
    Un = 1
    for n in range(etendue):
        Un = (sqrt(Un)+2)**2
    nb_pixel = Un
    hauteur = image.shape[0]
    largeur = image.shape[1]
    cimage = image.copy()

    for y in range(hauteur):
        for x in range(largeur):
            cmoy = [0,0,0]
            for cy in range(etendue*-1,etendue):
                for cx in range(etendue*-1,etendue):
                    
                    if y - cy < 0 or y+cy >= hauteur:
                        cy = 0
                    if x - cx < 0 or x + cx >= largeur:
                        cx = 0
                    #print(f'y:{y} x:{x}\ncy:{cy} cx:{cx}\n')
                    for c in range(3):
                        cmoy[c] += int(image[y+cy][x+cx][c]/nb_pixel)
            # print(image[y][x],cmoy)
            cimage[y][x] = cmoy
    return cimage

vg_img = imageio.imread('https://cgouygou.github.io/1NSI/T08_Extras/2Projets/images/vangogh/VanGogh_Arles.png')
#---------CONSOLE---------#
def menu(image = vg_img):

    def save(image):
        print("Image Générée !")
        savepath = str(input("Entrez le chemin de sauvegarde de l'image, en précisant son nom et son extension (.png, .jpeg) : "))
        imageio.imsave(savepath,image)
        print(f"Image sauvegardée à : {savepath}")

    hauteur = image.shape[0]
    largeur = image.shape[1]
   
    print(  "*********** IMAGE EDIT 2000 ***********")
    print(  "[0] Choisir une image   [5] Négatif\n",
            "[1] Filtre de couleur   [6] Flip\n",
            "[2] Pop Art             [7] Photomaton\n",
            "[3] Flop Art            [8] Pixel\n",
            "[4] Noir et Blanc       [9] Flou\n")

    chx = int(input("Entrez un nombre : "))

    if chx == 0 :
        pathimage = str(input("Entrez le chemin de l'image avec son nom et son extension : "))
        cimage = imageio.imread(pathimage)
        hauteur = image.shape[0]
        largeur = image.shape[1]
        print(f"Votre image : {pathimage}")
        menu(image = cimage)

    elif chx == 1:
        print("De quelle couleur doit être le filtre ?\n",
                "[1] Rouge  [2] Vert    [3] Bleu")
        chxcouleur = int(input("Entrez le numéro de la couleur: "))
        if chxcouleur == 1:
            couleur = 'rouge'
        elif chxcouleur == 2:
            couleur = 'vert'
        elif chxcouleur == 3:
            couleur = 'bleu'
        else:
            print("Numéro Invalide")
            menu()
        print("Génération de l'image . . .")
        for y in range(hauteur):
            for x in range(largeur):
                if len(image[y][x]) == 3:
                    R,G,B = image[y][x]
                    image[y][x] = filtre(R,G,B, couleur)
                else:
                    R,G,B,A = image[y][x]
                    image[y][x] = filtre(R,G,B, couleur)+ [A]
        save(image)
        
    elif chx == 2:
        print("Génération de l'image . . .")
        for y in range(hauteur):
            for x in range(largeur):
                if len(image[y][x]) == 3:
                    R,G,B = image[y][x]
                    image[y][x] = popart(R,G,B)
                else:
                    R,G,B,A = image[y][x]
                    image[y][x] = popart(R,G,B)+ [A]
        save(image)

    elif chx == 3:
        print("Génération de l'image . . .")
        for y in range(hauteur):
            for x in range(largeur):
                if len(image[y][x]) == 3:
                    R,G,B = image[y][x]
                    image[y][x] = flopart(R,G,B)
                else:
                    R,G,B,A = image[y][x]
                    image[y][x] = flopart(R,G,B)+ [A]
        save(image)

    elif chx == 4:
        print("Génération de l'image . . .")
        for y in range(hauteur):
            for x in range(largeur):
                if len(image[y][x]) == 3:
                    R,G,B = image[y][x]
                    image[y][x] = gris(R,G,B)
                else:
                    R,G,B,A = image[y][x]
                    image[y][x] = gris(R,G,B)+ [A]
        save(image)

    elif chx == 5:
        print("Génération de l'image . . .")
        for y in range(hauteur):
            for x in range(largeur):
                if len(image[y][x]) == 3:
                    R,G,B = image[y][x]
                    image[y][x] = negatif(R,G,B)
                else:
                    R,G,B,A = image[y][x]
                    image[y][x] = negatif(R,G,B) + [A]
        save(image)

    elif chx == 6:
        print("Génération de l'image . . .")
        image = flip(image)
        save(image)

    elif chx == 7:
        rep = int(input("Entrez un nombre de répitition : "))
        print("Génération de l'image . . . ")

        for n in range(rep):
            image = photomaton(image)
            
        save(image)

    elif chx == 8:
        print("Génération de l'image . . .")
        image = pixelisation(image)
        save(image)

    elif chx == 9:
        print("Génération de l'image . . . cela peut prendre un certains temps")
        image = flou(image)
        save(image)

    else:
        print("Choix Invalide, il doit correspondre au numéro de l'action que vous souhaitez éxecuter !")
        menu()
    

menu()
