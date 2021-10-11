from bigmod import BigMod
from xeuclidean import XEuclidean
from generator import GroupGenerator
import random

class Elgamal:
    def generate_key(self, p):
        g = GroupGenerator(p).find_random_generator()
        d = random.randrange(2, p - 1)
        e = BigMod().power(g, d, p)
        return (p, g, d, e)

    def encrypt(self, message, e, p, g):
        x = random.randrange(2, p - 1)
        c1 = BigMod().power(g, x, p)
        c2 = [BigMod().mul(c, BigMod().power(e, x, p), p) for c in self.encode(message)]

        return (c1, c2)

    def decrypt(self, d, c1, c2, p):
        ic1 = XEuclidean().inverse_modulo(BigMod().power(c1, d, p), p)
        return self.decode([BigMod().mul(ic1, int(c), p) for c in c2.rstrip().split(' ')])

    def encode(self, message):
        return [ord(c) for c in message]

    def decode(self, plain):
        return ''.join([chr(c) for c in plain])
