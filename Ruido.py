import random

import numpy as np


def addruido(i, senha, r=999999, g=0, b=0):
    im = i
    a = 0
    for i in senha:
        a += ord(i)
    random.seed(a=a, version=2)  # a=a
    w = im.size[0]
    h = im.size[1]
    tamanho = w * h

    #se não receber o ruido como parametro criar o ruido
    if r == 999999:
        r = []
        g = []
        b = []
        for i in range(tamanho):
            r.append(int(random.gauss(0, 2)))

        for i in range(tamanho):
            g.append(int(random.gauss(0, 2)))

        for i in range(tamanho):
            b.append(int(random.gauss(0, 2)))

    # Adiciona o rido recebio ou criado
    cont = 0
    for i in range(h):
        for j in range(w):
            if int(im.getpixel((j, i))[0] + r[cont]) > 255:
                r1 = 255
            elif int(im.getpixel((j, i))[0] + r[cont]) < 0:
                r1 = 0
            else:
                r1 = im.getpixel((j, i))[0] + r[cont]

            if int(im.getpixel((j, i))[1] + g[cont]) > 255:
                g1 = 255
            elif int(im.getpixel((j, i))[1] + g[cont]) < 0:
                g1 = 0
            else:
                g1 = im.getpixel((j, i))[1] + g[cont]

            if int(im.getpixel((j, i))[2] + b[cont]) > 255:
                b1 = im.getpixel((j, i))[2]
            elif int(im.getpixel((j, i))[2] + b[cont]) < 0:
                b1 = 0
            else:
                b1 = im.getpixel((j, i))[2] + b[cont]

            p = (r1, g1, b1)
            im.putpixel((j, i), p)
            cont += 1
    return im


def criaruido(i, senha):
    im = i
    a = 0
    for i in senha:
        a += ord(i)
    random.seed(a=a, version=2)  # a=a
    w = im.size[0]
    h = im.size[1]
    tamanho = w * h

    r = []
    g = []
    b = []
    for i in range(tamanho):
        r.append(int(random.gauss(0, 2)))

    for i in range(tamanho):
        g.append(int(random.gauss(0, 2)))

    for i in range(tamanho):
        b.append(int(random.gauss(0, 2)))

    ruido = np.array([r, g, b])
    return ruido
