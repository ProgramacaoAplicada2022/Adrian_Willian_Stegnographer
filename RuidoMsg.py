import random


def ruido(tamanho, senha, desv):
    a = 0
    for i in senha:
        a += ord(i)
    random.seed(a=a, version=2)  # a=a

    r = []
    for i in range(tamanho):
        r.append(int(random.gauss(0, desv)))
    return r
