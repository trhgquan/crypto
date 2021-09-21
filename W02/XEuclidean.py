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

  def solve_plain(self, a, b):
    print('a =', a)
    print('b =', b)

    print('GCD(a, b) =', self.extended_gcd(a, b)[0])
    print('a^-1 (mod b) =', self.inverse_modulo(a, b))

  def solve_csv(self, a, b):
    try:
      print(a, b, self.extended_gcd(a, b)[0], self.inverse_modulo(a, b), sep=',')
    except Exception:
      print(a, b, self.extended_gcd(a, b)[0], 'fail', sep=',')
