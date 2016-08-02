base = 3
mod = 17
mod = 2539

sk = input("Digite a chave secreta: ")
sk = int(sk)

print((base**sk) % mod)

ik = input("Digite a chave intermediaria: ")
ik = int(ik)

print((ik**sk) % mod)