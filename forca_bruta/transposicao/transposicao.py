import numpy as np
from math import ceil
from itertools import zip_longest
from sys import argv

words_english = open('../all_words.txt', 'r').read()
words_english = words_english.split()


escuro = open(argv[1], 'r').read()


def decifra(chave, data, name_file):
    chave = int(ceil(len(data) / chave))
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


for chave in range(1, 10**6):
    print(chave)
    msg = decifra(chave, escuro, None)
    lista_palavras = msg.split()

    words = []
    for word in lista_palavras[0:100]:
        if word in words_english:
            words.append(word)


    if(len(words) > 5):
        open('output_original', 'w').write(msg)
        print("Chave: " + str(chave))
        break