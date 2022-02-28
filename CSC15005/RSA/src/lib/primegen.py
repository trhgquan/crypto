from bigmod import BigMod
from xeuclidean import XEuclidean

class PrimeGen:
  def __init__(self, seed, collision = 1):
    self.__seed = seed
    self.__collision = collision

  def create(self, expected_length):
    p1 = self.__seed
    d1 = len(str(p1))

    while (d1 <= expected_length):
      found = 0
      for k1 in range(2, 2 * (p1 + 1) + 1):
        p2 = 2 * k1 * p1 + 1
        d2 = len(str(p2))

        if d2 > expected_length: break
        if p2 % 10 == 5: continue

        print('Testing {0} (k = {1})'.format(p2, k1))
        for a1 in range(2, p2 + 1, self.__collision):
          power_mod = BigMod.power(a1, k1 * p1, p2)
          extended_gcd = XEuclidean.extended_gcd(a1**k1 + 1, p2)[0]

          if power_mod == p2 - 1 and extended_gcd == 1:
            print(p2, ' valid')
            found = 1
            break

        if found == 1: break

      if found == 1:
        p1 = p2
        d1 = len(str(p1))

      if d2 >= expected_length: break

    return p1
