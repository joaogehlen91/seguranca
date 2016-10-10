import numpy as np
from math import ceil
from itertools import zip_longest
from sys import argv


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

    open(name_file, 'wb').write(bytes(msg_cifrada, 'utf-8'))


def decifra(chave, data, name_file):
    cifra(int(ceil(len(data) / chave)), data, name_file)


if len(argv) == 1:
    print("Use 'python transposicao' [file input] [-c cifrar | -d decifrar] [chave]")
else:
    file = open(argv[1], 'r')
    data = file.read()
    chave = int(argv[3])
    if argv[2] == '-c':
        cifra(chave, data, 'output_cifrado')
    else:
        decifra(chave, data, 'output_original')