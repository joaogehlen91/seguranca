from itertools import cycle
from sys import argv

file = open(argv[1], 'rb')
msg = file.read()

chave = str(argv[2])
chave = [ord(i) for i in chave]

#Cifra
msg_cifrada = bytes((c + m) % 256 for (c, m) in zip(cycle(chave), msg))
open('output_cifrado', 'wb').write(msg_cifrada)

#Decifra
chave = [-c for c in chave]
msg_decifrada = bytes((c + m) % 256 for (c, m) in zip(cycle(chave), msg_cifrada))
open('output_original', 'wb').write(msg_decifrada)

print("Feito!")