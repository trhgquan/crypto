from crypt import *

def encrypt(filename, key):
  with open(filename, 'r') as file:
    data = file.read()

  # return Type1_Encryptor(data, key).encrypt()
  return Type2_Encryptor(data, key).encrypt(True)

def decrypt(filename, key):
  with open(filename, 'r') as file:
    data = file.read()

  # return Type1_Decryptor(data, key).decrypt()
  return Type2_Decryptor(data, key).decrypt()

def main():
  # key = 3
  key = '4018975632'

  textFile = 'input.txt'
  result = encrypt(textFile, key)

  # encryptedFile = 'encrypted.txt'
  # result = decrypt(encryptedFile, key)

  print(result)

if  __name__ == "__main__":
  main()
