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

print(sha+"\n")
sha_encrypted = public_key.encrypt(sha, 32)
print(type(sha_encrypted))


fkey = open('key.pem', 'w').write(str(str_public_key))

fout = open('file_encrypted', 'w')
fout.write(str(text))
fout.write('\n')
fout.write(str(sha))
fout.write('\n')
fout.write(str(sha_encrypted))
fout.write('\n')
fout.write(str(str_public_key))
