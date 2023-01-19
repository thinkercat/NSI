import imageio

image = imageio.imread('/home/nsi/Documents/NSI/python/Exos/Irem/VoyageStegano.png')
print(f'{image.shape[0]}:{image.shape[1]}')

for h in range(image.shape[0]):
    for l in range(image.shape[1]):

        r = image[h][l][0]
        v = image[h][l][1]
        b = image[h][l][2]
        if b%2 == 0:
            rb = bin(r)


            if rb[len(rb)-2] == 'b':
                nv_gris = rb[len(rb)-1]
            elif rb[len(rb)-3] == 'b':
                nv_gris = rb[len(rb)-2]+rb[len(rb)-1]
            else:
                nv_gris = rb[len(rb)-3]+rb[len(rb)-2]+rb[len(rb)-1]
            
            nv_gris = int(nv_gris,2)
            
        else:            
            vb = bin(v)

            if vb[len(vb)-2] == 'b':
                nv_gris = vb[len(vb)-1]
            elif vb[len(vb)-3] == 'b':
                nv_gris = vb[len(vb)-2]+vb[len(vb)-1]
            else:
                nv_gris = vb[len(vb)-3]+vb[len(vb)-2]+vb[len(vb)-1]



            nv_gris = int(nv_gris,2)
        image[h][l][0] = 255//8*nv_gris
        image[h][l][1] = 255//8*nv_gris
        image[h][l][2] = 255//8*nv_gris


imageio.imsave('imagejhfdsmkjdhfjksdgfhsl.png',image)