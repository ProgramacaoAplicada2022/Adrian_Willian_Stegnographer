import random


def ruido(tamanho, senha, desv, r=999999, g=0, b=0):
    a = 0
    for i in senha:
        a += ord(i)
    random.seed(a=a, version=2)  # a=a

    # se não receber o ruido como parametro criar o ruido
    if r == 999999:
        r = []
        for i in range(tamanho):
            r.append(int(random.gauss(0, desv)))
    return r
