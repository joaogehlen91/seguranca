#pycrypto
#openSSL

from Crypto.Cipher import AES
from Crypto import Random

key = 'it chave com trinta e dois bytes'
iv = Random.new().read(AES.block_size)

cipher = AES.new(key, AES.MODE_CFB, iv)

msg = cipher.encrypt('joao miguel asd')

print(msg)


msg2 = AES.new(key, AES.MODE_CFB, iv)
a = msg2.decrypt(msg)

print(a)
