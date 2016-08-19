from Crypto.PublicKey import RSA
from Crypto import Random


random_generator = Random.new().read
key = RSA.generate(2048, random_generator)


publickey = key.publickey()
public_key = publickey.exportKey("PEM")
private_key = key.exportKey("PEM")


msg_encrypted = publickey.encrypt('esta mensagem foi criptografada e descriptografada', 32)



print '\nencrypted message:\n', msg_encrypted


#decrypted code below

decrypted = key.decrypt(msg_encrypted)

print '\ndecrypted:\n', decrypted
