from lib.bigmod import BigMod
from lib.xeuclidean import XEuclidean
from dh import DiffieHellman
import random

class SymetricDH(DiffieHellman):
    def generate_key(self, p):
        p, g = super().generate_key(p)
        x = random.randrange(2, p - 1)
        y = random.randrange(2, p - 1)
        ka = BigMod().power(g, x, p)
        kb = BigMod().power(g, y, p)
        return (p, g, ka, kb, x, y)

    def encrypt(self, message, key, power, p):
        key = BigMod().power(key, power, p)
        return [BigMod().mul(key, m, p) for m in self.encode(message)]

    def decrypt(self, cipher, key, power, p):
        key = XEuclidean().inverse_modulo(BigMod().power(key, power, p), p)
        return self.decode([BigMod().mul(int(c), key, p) for c in cipher.rstrip().split(' ')])
