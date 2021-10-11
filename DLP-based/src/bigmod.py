class BigMod:
  def add(self, x, y, n):
    return (x + y) % n

  def mul(self, x, y, n):
    p = 0

    x = x % n

    while y > 0:
      if y & 1:
        p = self.add(p, x, n)

      x = (x << 1) % n

      y = y >> 1

    return p

  def power(self, x, p, n):
    y = 1

    x = x % n

    if p == 0: return y

    while p > 0:
      if p & 1: y = self.mul(y, x, n)

      p = p >> 1

      x = self.mul(x, x, n)

    return y
