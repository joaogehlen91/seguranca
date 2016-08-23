from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random
import sys


fkey = open('key.pem', 'r')


key = RSA.importKey(fkey.read())


