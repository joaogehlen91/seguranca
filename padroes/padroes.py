lista = ['fofo', 'faca', 'bolo', 'fofo', 'fofa', 'tata', 'bola']

lista_padrao = {}


for w in lista:
	count = 0
	padrao = ''
	padrao_palavra = {}

	for c in w:
		if count == 0:
			padrao_palavra.update({c: count})
			padrao += str(count)
			count += 1
		else:
			if padrao_palavra.get(c) == None:
				padrao_palavra.update({c: count})
				padrao += str(count)
				count += 1
			else:
				padrao += str(padrao_palavra.get(c))
	
	lista_padrao.update({w: padrao})

print(lista_padrao)