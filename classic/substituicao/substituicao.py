from random import shuffle
from sys import argv

def inverte_chave(chave):
    return dict([(j, i) for (i, j) in chave.items()])

def gera_chave():
    try:
        file_key = open(argv[2], 'rb')
        f = file_key.read()
        key = dict(enumerate(f))
    except Exception:
        a = list(range(256))
        shuffle(a)
        key = dict(enumerate(a))
    return key


file = open(argv[1], 'rb')
msg = file.read()
key = gera_chave()

#cifrar
msg_cifrada = bytes(key[x] for x in msg)
open('output_cifrado', 'wb').write(msg_cifrada)

#decifra
key = inverte_chave(key)
msg_decifrada = bytes(key[x] for x in msg_cifrada)
open('output_original', 'wb').write(msg_decifrada)