chave_cifra = {
    'a':'x',
    'b':'d',
    'c':'s',
    'd':'k',
    'e':'p',
    'f':'i',
    'g':'o',
    'h':'q',
    'i':'c',
    'j':'t',
    'k':'u',
    'l':'e',
    'm':'v',
    'n':'j',
    'o':'r',
    'p':'a',
    'q':'m',
    'r':'g',
    's':'z',
    't':'y',
    'u':'b',
    'v':'w',
    'w':'h',
    'x':'l',
    'y':'n',
    'z':'f',
    ' ':'_'
}
chave_decifra = {}
for i in chave_cifra:
    chave_decifra.update({chave_cifra[i]:i})


mensagem = "atacar a base sul"

#Cifra
msg_cifrada = []
for i in mensagem:
    msg_cifrada.append(chave_cifra[i])

msg_cifrada = ''.join(msg_cifrada)
print('Mensagem cifrada: ' + msg_cifrada)

#Decifra
msg_decifrada = []
for i in msg_cifrada:
    msg_decifrada.append(chave_decifra[i])

msg_decifrada = ''.join(msg_decifrada)
print('Mensagem original: ' + msg_decifrada)
