import random


def addruido(i, senha):
    im = i
    a = 0
    for i in senha:
        a += ord(i)
    random.seed(a=None, version=2)  # a=a
    w = im.size[0]
    h = im.size[1]
    tamanho = w * h

    r = []
    g = []
    b = []
    for i in range(tamanho):
        r.append(int(random.gauss(0, 12)))

    for i in range(tamanho):
        g.append(int(random.gauss(0, 12)))

    for i in range(tamanho):
        b.append(int(random.gauss(0, 12)))

    cont = 0
    for i in range(h):
        for j in range(w):
            if (int(im.getpixel((j, i))[0] + r[cont]) > 255) or (int(im.getpixel((j, i))[0] + r[cont]) < 0):
                r1 = im.getpixel((j, i))[0]
            else:
                r1 = im.getpixel((j, i))[0] + r[cont]
            if (int(im.getpixel((j, i))[1] + g[cont]) > 255) or (int(im.getpixel((j, i))[1] + g[cont]) < 0):
                g1 = im.getpixel((j, i))[1]
            else:
                g1 = im.getpixel((j, i))[1] + g[cont]

            if (int(im.getpixel((j, i))[2] + b[cont]) > 255) or (int(im.getpixel((j, i))[2] + b[cont]) < 0):
                b1 = im.getpixel((j, i))[2]
            else:
                b1 = im.getpixel((j, i))[2] + b[cont]
            p = (r1, g1, b1)
            im.putpixel((j, i), p)
            cont += 1
    return im
