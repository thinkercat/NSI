import imageio

image = imageio.imread('python/Exos/img/pikachu.png')

hauteur = image.shape[0]
largeur = image.shape[1]

pixels = 0
for y in image:
    for pixel in image:
        print(pixel)
        if pixel != [0, 255, 0, 255]:
            pixels += 1

