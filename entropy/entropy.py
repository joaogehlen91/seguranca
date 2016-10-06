from math import log
from sys import argv
from tree import *


texto = 'a_casa_amarela'
texto = open(argv[1], 'rb').read()
#texto = [chr(x) for x in xrange(256)]
#texto = '00001111001100000000111111101101010101'
#base = 256


# Calcula a frquencia da aparicao de cada caractere no texto e armazena no set 'freq'
freq = {}
for c in texto:
	x = freq.get(c) or 0
	freq.update({c: x+1})

l = []
for i in freq:
	l.append(N(i, freq[i]))


l.sort()
print(l)

arvore = huffmann(l)
array = bitarray(endian='big')

for i in texto:
    array += arvore[i]

print(array)

open('saida_zip', 'wb').write(array.tobytes())





"""
# p eh a probabilidade de massa
acum = 0
for i in freq:
	p = float(freq[i]) / float(len(texto))
	acum += p * log(p, base)
acum = -acum

print(acum)
"""