msg = 'bolabalacasarosafacafofafofo'

size_token = 4
tokens = []

for i in xrange((len(msg) / size_token) + 1):
    token = msg[0:size_token]
    msg = msg[size_token:]
    tokens.append(token)


print(tokens)
