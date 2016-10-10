import numpy as np
from math import ceil
from itertools import zip_longest
from sys import argv

claro = open(argv[1], 'r').read()
escuro = open(argv[2], 'r').read()


def cifra(chave, data, name_file):
    lista = []
    matriz = []

    for x in range(0, len(data), chave):
        lista.append(data[x:x+chave])

    z = zip_longest(*lista, fillvalue='#')

    for i in z:
        matriz.append(list(i))

    matriz_t = np.array(matriz).tolist()

    msg = [j for i in matriz_t for j in i]
    msg_cifrada = ''.join(msg)

    return(msg_cifrada)


for chave in range(1, len(escuro)):
    msg = cifra(chave, claro, None)
    if msg[0:1000] == escuro[0:1000]:
        break