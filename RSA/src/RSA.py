from lib.bigmod import BigMod
from lib.xeuclidean import XEuclidean
import random

class RSA:
    @staticmethod
    def generate(p, q) -> tuple:
        '''Generate public and private key from a pair of prime p and q

        Input:
          - p : first prime
          - q : second prime

        Output:
          - n : Public n
          - e : Public decryption key
          - d : Private decryption key
        '''
        n = p * q
        phi = (p - 1) * (q - 1)

        d, e = None, None

        while e is None:
            try:
                d = random.randint(2, phi - 1)
                e = XEuclidean.inverse_modulo(d, phi)
            except:
                pass

        return (n, e, d)

    @staticmethod
    def encrypt(message, public_key, n) -> list:
        '''Encrypt a message

        Input:
           - message : message string
           - public_key : RSA public key
           - n : Public n

        Output:
        '''
        return [BigMod.power(m, public_key, n) for m in RSA.encode(message)]

    @staticmethod
    def decrypt(cipher: str, private_key: int, n: int) -> str:
        '''Decrypt a message

        Input:
           - cipher : cipher string
           - private_key : RSA private key
           - n : Public n

        Output:
        '''
        return RSA.decode(
            [BigMod.power(int(c), private_key, n) for c in cipher.rstrip().split(' ')]
        )

    @staticmethod
    def encode(message: str) -> list:
        '''Encode a message to array of integers

        Input:
          - message : string message
        '''
        return [ord(c) for c in message]

    @staticmethod
    def decode(plain: list) -> str:
        '''Decode a message from list of integers.
        (aka convert it from integers to ASCII).

        Input:
          - plain : list of plaintext
        '''
        return ''.join([chr(c) for c in plain])
