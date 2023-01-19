import imageio

def main():
    
    PATH = "python/Exos/img/incrustation/"
    COLOR = [0,255,0]

    fond = imageio.imread("/home/nsi/Documents/NSI/python/Exos/img/icrustation/lycmdv_crop.png")
    incrust = imageio.imread("/home/nsi/Documents/NSI/python/Exos/img/icrustation/john.png")
    
    for h in range(fond.shape[0]):
        for l in range(fond.shape[1]):
            if incrust[h][l][0] < 10 and incrust[h][l][1] > 50 and incrust[h][l][2] < 10:
                    incrust[h][l][0] = fond[h][l][0]
                    incrust[h][l][1] = fond[h][l][1]
                    incrust[h][l][2] = fond[h][l][2]

                


    imageio.imsave('incrust.png',incrust)



if '__main__' == __name__ :
    main()