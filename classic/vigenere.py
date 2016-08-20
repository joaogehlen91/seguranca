alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

msg = "ATACARBASESUL"
chave = "LIMAO"

chave = chave * (len(msg)/len(chave)+1)

msg_chave = zip(msg, chave)
msg_cifrada = [alfabeto[(alfabeto.index(x) + alfabeto.index(y)) % 26] for x, y in msg_chave]
msg_cifrada = ''.join(msg_cifrada)
print(msg_cifrada)

msg_cifrada_chave = zip(msg_cifrada, chave)
msg_decifrada = [alfabeto[(alfabeto.index(x) - alfabeto.index(y)) % 26] for x, y in msg_cifrada_chave]
msg_decifrada = ''.join(msg_decifrada)
print(msg_decifrada)