class XEuclidean:
  def extended_gcd(self, a, b):
    if a == 0:
      return b, 0, 1

    g, y, x = self.extended_gcd(b % a, a)
    return g, x - (b // a) * y, y

  def inverse_modulo(self, a, m):
    g, x, y = self.extended_gcd(a, m)

    if g != 1:
      raise Exception('Inverse modular does not exist.')
    return x % m
