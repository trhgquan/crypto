from random import *
import sys

def egcd(a, b):
  if a == 0:
    return (b, 0, 1)
  else:
    g, y, x = egcd(b % a, a)
    return (g, x - (b // a) * y, y)

def modinv(a, m):
  g, x, y = egcd(a, m)
  if g != 1:
    return 'fail'
  else:
    return x % m

def solve(a, b):
  print(a, b, egcd(a, b)[0], modinv(a, b), sep=',')
    
def main():
  with open('result.csv', 'w+') as f:
    sys.stdout = f

    for i in range(0, 100):
      a = randrange(0, 1337)
      b = randrange(0, 1337)

    solve(a, b)

if __name__ == '__main__':
  main()
