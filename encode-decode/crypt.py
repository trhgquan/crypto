class Encryptor:
  def __init__(self, plain, key):
    self.plain = plain
    self.key = key

  def encrypted_charcode(self, char):
    pass

  def encrypt(self):
    pass

class Type1_Encryptor(Encryptor):
  def encrypted_charcode(self, char):
    new_char = (ord(char) - 97 + self.key) % 26 + 1
    return str(0) + str(new_char) if new_char < 10 else str(new_char)

  def encrypt(self, raw = False):
    result = ''

    for c in self.plain:
      c = c.lower()
      if c in [' ', ',', '.', '\n']: result += c
      else:
        result += (chr(int(self.encrypted_charcode(c)) + 97), self.encrypted_charcode(c)) [raw]

    return result

class Type2_Encryptor(Encryptor):
  def __init__(self, plain, key):
    super().__init__(plain, key)

    self.sigma = {str(value):str(name) for value, name in enumerate([char for char in key])}
  
  def encrypted_charcode(self, char):
    char = (ord(char) - 97) % 26;
    char = str(0) + str(char) if char < 10 else str(char)

    new_char = ''

    for c in char:
      new_char += self.sigma[c]

    return new_char


  def encrypt(self, raw = False):
    result = ''

    for c in self.plain:
      if c in [' ', ',', '.', '\n']: result += c
      else:
        if raw:
          result += self.encrypted_charcode(c)
        else:
          for digit in self.encrypted_charcode(c):
            result += chr(int(digit) + 97)

    return result

class Decryptor:
  def __init__(self, string, key):
    self.string = string
    self.key = key

  def plain_charcode(self, current):
    pass

  def decrypt(self):
    pass

class Type1_Decryptor(Decryptor):
  def plain_charcode(self, char):
    char = (ord(char) - 97 - self.key) % 26 - 1
    return str(0) + str(char) if char < 10 else str(char)

  def decrypt(self, raw = False):
    result = ''

    for c in self.string:
      if c in [' ', '.', ',', '\n']: result += c
      else:
        result += (chr(int(self.plain_charcode(c)) + 97), self.plain_charcode(c))[raw]

    return result

class Type2_Decryptor(Decryptor):
  def __init__(self, string, key):
    super().__init__(string, key)

    self.sigma = {str(name):str(value) for value, name in enumerate([char for char in key])}

  def plain_charcode(self, current):
    char = ''
    
    for c in current:
      char += self.sigma[str(ord(c) - 97)]

    return char

  def decrypt(self, raw = False):
    result = ''

    while self.string:
      if self.string[0] in [' ', '.', ',', '\n']:
        result += self.string[0]
        self.string = self.string[1:]
      else:
        result += (chr(int(self.plain_charcode(self.string[:2])) + 97), self.plain_charcode(self.string[:2]))[raw]
        self.string = self.string[2:]

    return result
