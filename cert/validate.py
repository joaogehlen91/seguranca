from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random
import sys


#Chave publica
fkey = open('key.pem', 'r')
public_key = RSA.importKey(fkey.read())


#Arquivo 
file = open(sys.argv[1], 'r')
list_text = file.readlines()
text = list_text[0].replace('\n', '')
signature_orig = list_text[2].replace('\n', '')


hash = SHA256.new()
hash.update(text)
sha = hash.digest()

signature = public_key.encrypt(sha, 32)


if str(signature) == str(signature_orig):
    print("Assinatura valida")
else:
    print("Assinatura invalida")
