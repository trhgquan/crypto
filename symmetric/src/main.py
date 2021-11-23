from matrix_cipher import MatrixCipher
import time

def main():
    with open('input.txt', 'r+') as f:
        message = f.readline().strip()

    print('message')
    print(message)


    mc = MatrixCipher(10, 2)

    cipher = mc.encrypt(message)


    with open('cipher.txt', 'w+') as f:                
        print('cipher', file = f)
        print(cipher, file = f)

        print('cipher')
        print(cipher)

    with open('decrypted.txt', 'w+') as f:
        print('decrypted', file = f)
        print(mc.decrypt(cipher), file = f)

if __name__ == '__main__':
    start_time = time.time()
    
    main()

    print('Execute time: %s seconds' % (time.time() - start_time)
)
