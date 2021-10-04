from bigmod import *
from xeuclidean import *

class RSA:
  def generate(self, p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
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
    result = ''

    for c in plain:
      result += chr(c)

    return result
