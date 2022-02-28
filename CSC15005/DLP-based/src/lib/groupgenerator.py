from lib.bigmod import BigMod
from functools import reduce
import random

class GroupGenerator:
    def __init__(self, n):
        self.__n = n

    def factors(self, n : int) -> set:
        '''Get prime factors of an integer

        Input:
            - n : int
        
        Output:
            - set of distinct prime factors
        '''
        return set(reduce(list.__add__,
                    ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

    def naive_list(self):
        '''Get generators list of this group
        '''
        for i in range(2, self.__n):
            is_generator = True
            power = 1
            generated = []
            while 1:
                m = BigMod.power(i, power, self.__n)
                if (m not in generated):
                    generated.append(m)
                else: break
                power += 1

            if len(generated) != self.__n - 1: is_generator = False

            if is_generator: print(i)

    def find_random_generator(self) -> int:
        '''Find a random generator

        Output:
            - int
        '''
        while 1:
            x = random.randrange(2, self.__n)
            is_generator = True
            for i in self.factors(self.__n - 1):
                if i == 1: continue
                k = (self.__n - 1) // i
                if BigMod.power(x, k, self.__n) == 1:
                    is_generator = False
                    break
            if is_generator: return x
