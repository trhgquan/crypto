import numpy as np
import numpy.matlib
import random
from lib.xeuclidean import XEuclidean

class MatrixCipher:
    def __init__(self, n, p):
        self.__n = n
        self.__p = p

        self.__encryption_key, self.__decryption_key = [], []
        for i in range(0, self.__n):
            e, d = self.keygen()
            self.__encryption_key.append(e)
            self.__decryption_key.append(d)

    '''
    Generate key
    '''
    def keygen(self):
        '''
        Generate an upper-triangular matrix with determinant != 0
        '''

        u_seed = np.random.randint(self.__p, size = (self.__n, self.__n))
        for i in range(0, self.__n):
            u_seed[i, i] = random.randint(1, self.__p - 1) if u_seed[i, i] == 0 else u_seed[i, i]
        u = np.matrix(np.triu(u_seed))

        '''
        Generate an lower-triangular matrix with determinant != 0
        '''

        l_seed = np.random.randint(self.__p, size = (self.__n, self.__n))
        for i in range(0, self.__n):
            l_seed[i, i] = random.randint(1, self.__p - 1) if l_seed[i, i] == 0 else l_seed[i, i]
        l = np.matrix(np.tril(l_seed))

        
        '''
        Creating encryption key K = l * u
        '''
        encryption_key = (l * u) % self.__p


        '''
        Some magics to find decryption key K^{-1}.
        Just kidding. This is linear algebra.
        '''
        bases = np.matlib.identity(self.__n)

        y = []
        y.append(bases[:, 0] * XEuclidean().inverse_modulo(l[0, 0], self.__p))
        for i in range(1, self.__n):
            sum_ = 0
            for j in range(0, i):
                sum_ += (y[j] * l[i, j]) % self.__p
            sum_ %= self.__p
            y.append(np.array(((bases[:, i] - sum_) * XEuclidean().inverse_modulo(l[i, i], self.__p)) % self.__p))

        y = np.matrix(np.column_stack(y)).transpose()

        x = [0] * self.__n
        x[self.__n - 1] = y[self.__n - 1, :] * XEuclidean().inverse_modulo(u[self.__n - 1, self.__n - 1], self.__p)
        for i in range(self.__n - 2, -1, -1):
            sum_= 0
            for j in range(i + 1, self.__n):
                sum_ += (x[j] * u[i, j]) % self.__p
            sum_ %= self.__p

            x[i] = np.array(((y[i, :] - sum_) * XEuclidean().inverse_modulo(u[i, i], self.__p)) % self.__p)

        decryption_key = np.matrix(np.reshape(x, (self.__n, self.__n)))

        return encryption_key, decryption_key

    '''
    Convert message to nx1 matrices (calculatable format)
    '''
    def chunks(self, message):
        list_messages = (message[0 + i:self.__n + i] for i in range(0, len(message), self.__n))

        list_calculatable = []
        for m in list(list_messages):
            numered_array = np.array([[int(i) for i in m]], order = 'C')
            numered_array.resize(self.__n, 1)
            list_calculatable.append(np.matrix(numered_array))

        return list_calculatable


    '''
    Encrypt message
    '''
    def encrypt(self, message):
        cipher, cipher_temp = '', []
        message = self.chunks(message)

        for i, val in enumerate(message):
            current_key = (i - (i % 100)) % 100
            c = (self.__encryption_key[current_key] * val) % self.__p
            cipher_temp.append(np.reshape(np.array(c), (1, -1)))


        for c in cipher_temp:
            cipher += ''.join(str(int(i)) for i in c[0])
        
        return cipher

    '''
    Decrypt message
    '''
    def decrypt(self, cipher):
        message, message_temp = '', []
        cipher = self.chunks(cipher)

        for i, val in enumerate(cipher):
            current_key = (i - (i % 100)) % 100
            m = (self.__decryption_key[current_key] * val) % self.__p
            message_temp.append(np.reshape(np.array(m), (1, -1)))

        for m in message_temp:
            message += ''.join(str(int(i)) for i in m[0])
        
        return message

    def encryption_key(self):
        return self.__encryption_key

    def decryption_key(self):
        return self.__decryption_key
