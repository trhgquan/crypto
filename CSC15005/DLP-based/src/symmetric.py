from lib.bigmod import BigMod
from lib.xeuclidean import XEuclidean
from dh import DiffieHellman
import random

class SymmetricDH(DiffieHellman):
    @staticmethod
    def generate_key(p : int) -> tuple:
        '''Generate keypair

        Input:
            - p : (Z_p)
        
        Output:
            - p : (Z_p)
            - g : Generator of (Z_p)
            - ka, kb : key for a and b
            - x, y: ka^x = kb^y = k (encrypt / decrypt key)
        '''
        p, g = DiffieHellman.generate_key(p)
        x, y = random.randrange(2, p - 1), random.randrange(2, p - 1)
        ka, kb = BigMod.power(g, x, p), BigMod.power(g, y, p)
        
        return (p, g, ka, kb, x, y)

    @staticmethod
    def encrypt(message : str, key : int, power : int, p : int) -> list:
        '''Encrypt a message
        cipher = key*m; key = ka^x = kb^y

        Input:
            - message : Message to encrypt
            - key : int
            - power : int
            - p : int
        
        Output:
            - Cipher (as a list). This should be stored as a string (later).
        '''
        key = BigMod.power(key, power, p)
        return [BigMod.mul(key, m, p) for m in SymmetricDH.encode(message)]

    @staticmethod
    def decrypt(cipher : str, key : int, power : int, p : int) -> str:
        '''Decrypt a cipher

        Input:
            - cipher : string
            - key : int
            - power : int
            - p : int
        
        Output:
            - Plaintext (string)
        '''
        key = XEuclidean.inverse_modulo(BigMod.power(key, power, p), p)
        return SymmetricDH.decode([BigMod.mul(int(c), key, p) for c in cipher.rstrip().split(' ')])

    # Using XOR operator - don't need inverse modulo and bigint multiply.
    @staticmethod
    def encrypt_xor(message, key, power, p) -> list:
        '''Encrypt a message, using XOR operator

        Input:
            - message : Message to encrypt
            - key : int
            - power : int
            - p : int
        
        Output:
            - Cipher (as a list). This should be stored as a string (later).
        '''
        key = BigMod.power(key, power, p)
        return [m ^ key for m in SymmetricDH.encode(message)]

    @staticmethod
    def decrypt_xor(cipher : str, key : int, power : int, p : int) -> str:
        '''Decrypt a cipher, using XOR operator

        Input:
            - cipher : string
            - key : int
            - power : int
            - p : int
        
        Output:
            - Plaintext (string)
        '''
        key = BigMod.power(key, power, p)
        return SymmetricDH.decode([(int(c) ^ key) for c in cipher.rstrip().split(' ')])
