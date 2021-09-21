from random import *
import sys

class Euclidean:
  def __init__(self, a, b):
    self.a = a
    self.b = b

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

  def solve(self):
    print('a =', self.a)
    print('b =', self.b)

    print('GCD(a, b) =', self.extended_gcd(self.a, self.b)[0])
    print('a^-1 (mod b) =', self.inverse_modulo(self.a, self.b))

def main():
  a = int(input('a = '))
  b = int(input('b = '))

  try:
    test = Euclidean(a, b)
    test.solve()
  except Exception as message:
    print(message)

if __name__ == '__main__':
  main()
