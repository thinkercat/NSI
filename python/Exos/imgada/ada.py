import imageio

image = imageio.imread('python/Exos/imgada/ada.png')

hauteur = image.shape[0]
largeur = image.shape[1]

point1 = [120,100]
point2 = [140,200]

for y in image :
    if y == 120:
        image[140][200] = [255,0,0,255]

imageio.imsave('adamoustache.png',image)