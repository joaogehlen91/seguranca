from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random
import sys


file = open(sys.argv[1], 'r')
text = file.read()


hash = SHA256.new()
hash.update(text)
sha = hash.digest()


text_sha = text + "\n" + sha


""" gera chave publica e privada """
random_generator = Random.new().read
key = RSA.generate(2048, random_generator)
public_key = key.publickey()
str_public_key = public_key.exportKey("PEM")
str_private_key = key.exportKey("PEM")
#print(str_public_key)
#print(str_private_key)


msg_encrypted = public_key.encrypt(text_sha, 2048)
# tentar gerar AES e depois RSA
print(msg_encrypted)




fout = open('file_encrypted', 'w')
fout.write(text)
fout.write('\n')
fout.write(sha)
