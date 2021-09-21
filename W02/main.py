from XEuclidean import *
import random
import sys

def main():
  # a = int(input('a = '))
  # b = int(input('b = '))

  # try:
  #  XEuclidean().solve(a, b)
  # except Exception as message:
  #  print(message)

  with open('result.csv', 'w+') as f:
    sys.stdout = f

    for i in range(100):
      a = random.randint(1, 1337)
      b = random.randint(1, 1337)

      XEuclidean().solve_csv(a, b)

if __name__ == '__main__':
  main()
