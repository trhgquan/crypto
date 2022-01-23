class BigMod:
    @staticmethod
    def add(x: int, y: int, n: int) -> int:
        '''(x + y) % n

        Input:
            - x : int
            - y : int
            - n : int
        
        Output:
            - int
        '''
        return (x + y) % n

    @staticmethod
    def mul(x : int, y : int, n : int) -> int:
        '''Quick multiply, then modulo n

        Input:
            - x : int
            - y : int
            - n : int
        
        Output:
            - int
        '''
        p = 0

        x = x % n

        while y > 0:
            if y & 1:
                p = BigMod.add(p, x, n)

            x = (x << 1) % n

            y = y >> 1

        return p

    @staticmethod
    def power(x : int, p : int, n : int) -> int:
        '''Quick power x^p, modular n

        Input:
            - x : int
            - p : int
            - n : int
        
        Output:
            - int
        '''
        y = 1

        x = x % n

        if p == 0:
            return y

        while p > 0:
            if p & 1:
                y = BigMod.mul(y, x, n)

            p = p >> 1

            x = BigMod.mul(x, x, n)

        return y
