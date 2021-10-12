from elgamal import Elgamal

def main():
    # Generate key for encryption / decryption
    p, g, d, e = Elgamal().generate_key(269)
    print(p, g, d, e, sep = ', ')

    # p, g, d, e = 269, 237, 166, 89

    # Encryption
    # with open('test.txt', 'r+') as f:
    #     message = f.read()
    #
    # encrypted_content = Elgamal().encrypt(message, e, p, g)
    #
    # print(encrypted_content[0])
    # print(*encrypted_content[1], sep=' ')

    # Decryption
    # with open('encrypted.txt', 'r+') as f:
    #     c1 = int(f.readline())
    #     c2 = f.readline()
    #     print(Elgamal().decrypt(d, c1, c2, p))

if __name__ == '__main__':
    main()
