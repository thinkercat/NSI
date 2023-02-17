import imageio.v2 as imageio

def invertBin(color :int)->int:
    # 5 -> 101
    bin_color = bin(color).split('0b')[1]

    # 110 -> ['0', '1', '1']
    inverted_bin = []
    for i in range(len(bin_color)):
        inverted_bin.append(bin_color[(-1)*i])
    inverted_bin.append(inverted_bin.pop(0))
    print(bin_color,':',inverted_bin)

    # liste -> str
    s = ''
    for e in inverted_bin:
        s += e

    if int(s,2) > 255:
        return 255
    else:
        return int(s,2)

img = imageio.imread("https://pydefis.callicode.fr/defis/static/cup2019/portrait.png")

for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        for c in range(img.shape[2]):
            img[y][x][c] = invertBin(img[y][x][c]) 

imageio.imsave('portrait.png',img)