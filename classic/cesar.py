msg = "Isso e secreto"
chave = 5

""" Cifra """
msg_cifrada = [chr((ord(x) + chave) % 256) for x in msg]
msg_cifrada = ''.join(msg_cifrada)
print('Mensagem cifrada:\n' + msg_cifrada)

""" Decifra """
msg_decifrada = [chr((ord(x) - chave) % 256) for x in msg_cifrada]
msg_decifrada = ''.join(msg_decifrada)
print('Mensagem decifrada:\n' + msg_decifrada)