import numpy as np


mensagem = "esta mensagem era pra ser um segredo"
chave = 3
som = chave


l_mensagem = list(mensagem)
for x in xrange(len(mensagem) % chave):
    l_mensagem.append('#')

matriz = []
linha = []

for x in xrange(len(l_mensagem)):
    linha.append(l_mensagem[x])
    if x == chave-1:
        matriz.append(linha)
        linha = []
        chave += som

#print(matriz)
matriz_t = np.array(matriz)
matriz_t = matriz_t.transpose().tolist()
#print(matriz_t)


#Formatar matriz para mostrar mensagem cifrada
lista = [j for i in matriz_t for j in i]
msg_cifrada = ''.join(lista)
print("Mensagem cifrada:\n" + msg_cifrada+"\n")