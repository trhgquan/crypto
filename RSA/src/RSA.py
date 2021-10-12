from lib.bigmod import BigMod
from lib.xeuclidean import XEuclidean

class RSA:
  def generate(self, p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    # Given that d should be in (1, phi) and coprime with phi.
    # Since p and q are primes, phi = (p - 1) * (q - 1) will even
    # and (p + q) // 2 will be an odd. Therefore, GCD((p + q) // 2, phi) = 1
    d = (p + q) // 2

    e = XEuclidean().inverse_modulo(d, phi)

    return (n, e, d)

  def encrypt(self, message, public_key, n):
    return [BigMod().power(m, public_key, n) for m in self.encode(message)]

  def decrypt(self, message, private_key, n):
    return self.decode([BigMod().power(int(c), private_key, n) for c in message.rstrip().split(' ')])

  def encode(self, message):
    return [ord(c) for c in message]

  def decode(self, plain):
    return ''.join([chr(c) for c in plain])
