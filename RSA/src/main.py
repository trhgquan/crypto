from RSA import *

def main():
  n, e, d = RSA().generate(9337, 2293)

  # with open('test.txt', 'r') as file:
  #   message = file.read()
  #   for c in RSA().encrypt(message, e, n):
  #     print(c, end=' ')

  # with open('encrypted.txt', 'r') as file:
  #   cipher = file.read()
  #   print(RSA().decrypt(cipher, d, n))

if __name__ == '__main__':
  main()
