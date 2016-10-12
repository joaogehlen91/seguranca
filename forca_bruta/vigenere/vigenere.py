from itertools import cycle
from sys import argv
import itertools

lista = '0123456789abcdefghijklmnopqrstuvwxyz'

data = open(argv[1], 'rb').read()

words_english = open('../all_words.txt', 'rb').read()
words_english = words_english.split()

chaves_invalidas = []

for i in range(1, 4):
    r = itertools.product(lista, repeat=i)
    for i in r:
        #if i in chaves_invalidas:
        #    continue
        print(i)
        chave = [-ord(j) for j in i]
        msg_decifrada = bytes((c + m) % 256 for (c, m) in zip(cycle(chave), data))
        lista_palavras = msg_decifrada.split()
        
        words = []
        for word in lista_palavras[0:30]:
            if word in words_english:
                words.append(word)

        if(len(words) > 5):
            open('output_original', 'wb').write(msg_decifrada)
            print("Chave: " + str(i))
            if input("Texto estah bom? (s=sim/n=nao)") == 's':
                print("Descriptografado")
                break