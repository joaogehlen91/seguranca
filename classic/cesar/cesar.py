from sys import argv

file = open(argv[1], 'rb')
data = file.read()
chave = int(argv[3])


def cifra():
    open('output_cifrado', 'wb').write(bytes((l + chave) % 256 for l in data))


def decifra():
    open('output_original', 'wb').write(bytes((l + chave*-1) % 256 for l in data))


if argv[2] == '-c':
    cifra()
else:
    decifra()