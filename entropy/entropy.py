from math import log
from sys import argv


texto = 'teste_de_entropia'
#texto = [chr(x) for x in xrange(256)]
texto = '000011110011001101010101'
base = 2


# Calcula a frquencia da aparicao de cada caractere no texto e armazena no set 'freq'
freq = {}
for c in texto:
	x = freq.get(c) or 0
	freq.update({c: x+1})

# p eh a probabilidade de massa
acum = 0
for i in freq:
	p = float(freq[i]) / float(len(texto))
	acum += p * log(p, base)
acum = -acum

print(acum)
