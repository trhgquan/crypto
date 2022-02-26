from matrix_cipher import MatrixCipher
import time

def main():
    with open('input.txt', 'r+') as f:
        message = f.readline().strip()

    print('message')
    print(message)

    '''
    n = 10 -> dimensions of a square matrix.
    This also means we'll split the message into chunks of 10.
    (for matrix multiplication)
    
    p = 2 -> Since we're doing in binary.
    If there is an alphabet, this should be replaced by a prime.
    '''
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

    print('Execution time: %s seconds' % (time.time() - start_time))
