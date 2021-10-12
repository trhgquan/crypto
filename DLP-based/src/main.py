from elgamal import Elgamal
from symetricdh import SymetricDH

def demo_elgamal():
    # Generate key for encryption / decryption
    p, g, d, e = Elgamal().generate_key(269)
    print(p, g, d, e, sep = ', ')

    # p, g, d, e = 269, 237, 166, 89

    # Encryption
    # with open('test.txt', 'r+') as f:
    #     message = f.read()
    # encrypted_content = Elgamal().encrypt(message, e, p, g)
    # print(encrypted_content[0])
    # print(*encrypted_content[1], sep=' ')

    # Decryption
    # with open('encrypted-elgamal.txt', 'r+') as f:
    #     c1 = int(f.readline())
    #     c2 = f.readline()
    # print(Elgamal().decrypt(d, c1, c2, p))

def demo_symetric():
    # Generate key
    p, g, ka, kb, x, y = SymetricDH().generate_key(269)
    print(p, g, ka, kb, x, y, sep = ', ')

    # p, g, ka, kb, x, y = 269, 86, 197, 165, 117, 61

    # Encryption
    # with open('test.txt', 'r+') as f:
    #     message = f.read()
    # print(*SymetricDH().encrypt(message, ka, y, p), sep = ' ')

    # Decryption
    # with open('encrypted-symetric.txt', 'r+') as f:
    #     cipher = f.read()
    # print(SymetricDH().decrypt(cipher, kb, x, p))

def main():
    # Uncomment above function and call them here.

    # demo_elgamal()
    # demo_symetric()

    pass

if __name__ == '__main__':
    main()
