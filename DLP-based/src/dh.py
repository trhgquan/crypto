from lib.groupgenerator import GroupGenerator
import random

class DiffieHellman:
    def generate_key(self, p):
        g = GroupGenerator(p).find_random_generator()
        return (p, g)

    def encrypt(self):
        pass

    def decrypt(self):
        pass

    def encode(self, message):
        return [ord(c) for c in message]

    def decode(self, plain):
        return ''.join([chr(c) for c in plain])
