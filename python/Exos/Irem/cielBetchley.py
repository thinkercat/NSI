import imageio

image = imageio.imread('/home/nsi/Documents/NSI/python/Exos/Irem/pictureB.png')
bleu = []
for h in range(image.shape[0]):
    for l in range(image.shape[1]):

        bleu.append(str(image[h][l][2]))
        if image[h][l][2] == 127:
            image[h][l][0] = 0
            image[h][l][1] = 0
            image[h][l][2] = 0
        else:
            image[h][l][0] = 255
            image[h][l][1] = 255
            image[h][l][2] = 255

imageio.imsave('imagen.png',image)
print(f'{image.shape[0]}:{image.shape[1]}\n')

with open('bleu.txt','w') as file:
    for e in bleu:

        file.write(e)