from crypt import *

def encrypt_firstType(filename, key):
  with open(filename, 'r') as file:
    data = file.read()

  return Type1_Encryptor(data, key).encrypt()

def encrypt_secondType(filename, key):
  with open(filename, 'r') as file:
    data = file.read()

  return Type2_Encryptor(data, key).encrypt()


def decrypt_firstType(filename, key):
  with open(filename, 'r') as file:
    data = file.read()

  return Type1_Decryptor(data, key).decrypt()

def decrypt_secondType(filename, key):
  with open(filename, 'r') as file:
    data = file.read()

  return Type2_Decryptor(data, key).decrypt()

def main():

  '''
  First type: c = (m + k) % 26 + 1
  '''
  
  key = 3

  textFile = 'input.txt'
  result = encrypt_firstType(textFile, key)

  print(result)

  # NOTICE: inside encrypted_1.txt is first-type encrypted cipher.
  encryptedFile = 'encrypted_1.txt'
  result = decrypt_firstType(encryptedFile, key)

  print(result)

  '''
  Second type: c = sigma(m) with sigma(i) replace i with i-th key of k.
  '''

  key = '4018975632'

  textFile = 'input.txt'
  result = encrypt_secondType(textFile, key)

  print(result)

  # NOTICE: inside encrypted_2.txt is second-type encrypted cipher.
  encryptedFile = 'encrypted_2.txt'
  result = decrypt_secondType(encryptedFile, key)
  
  print(result)

if  __name__ == "__main__":
  main()
