from lib.bigmod import BigMod
from lib.xeuclidean import XEuclidean
from dh import DiffieHellman
import random

class Elgamal(DiffieHellman):
    def generate_key(self, p):
        p, g = super().generate_key(p)
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
