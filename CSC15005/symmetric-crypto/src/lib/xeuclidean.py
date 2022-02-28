class XEuclidean:
    @staticmethod
    def extended_gcd(a: int, b: int) -> tuple:
        '''Extended GCD

        Input:
            - a : int
            - b : int
        
        Output:
            - g : GCD(a, b)
            - x, y : ax + by = g (Bezout)
        '''
        if a == 0:
            return b, 0, 1

        g, y, x = XEuclidean.extended_gcd(b % a, a)
        return g, x - (b // a) * y, y

    @staticmethod
    def inverse_modulo(a : int, m : int) -> int:
        '''Finding inverse modulo of a in m

        Input:
            - a : int
            - m : int
        
        Output:
            - a^{-1}
        
        Exception
            - if inverse modular of a in m does not exist.
        '''
        g, x, _ = XEuclidean.extended_gcd(a, m)

        if g != 1:
            raise Exception('Inverse modular does not exist.')
        return x % m
