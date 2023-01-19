import imageio

image = imageio.imread('/home/nsi/Documents/NSI/python/Exos/Irem/whoami.png')
wikiimage = imageio.imread('/home/nsi/Documents/NSI/python/Exos/Irem/Ada_Lovelace_child_portrait_Somerville_College.jpg')

print(f'{image.shape}\n{wikiimage.shape}')


for h in range(image.shape[0]):
    for l in range(image.shape[1]):
        if wikiimage[h][l][0] == image[h][l][0] and wikiimage[h][l][1] == image[h][l][1] and wikiimage[h][l][2] == image[h][l][2]:
            image[h][l][0] = 0
            image[h][l][1] = 0
            image[h][l][2] = 0
        else:
            image[h][l][0] = 255
            image[h][l][1] = 255
            image[h][l][2] = 255            
imageio.imsave('adal.png',image)