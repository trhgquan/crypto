from lib.groupgenerator import GroupGenerator

class DiffieHellman:
    @staticmethod
    def generate_key(p : int) -> tuple:
        '''Generate a random group generator

        Input:
            - p : int
        
        Output:
            - p : original (Z_p)
            - g : generator of (Z_p)
        '''
        g = GroupGenerator(p).find_random_generator()
        return (p, g)

    @staticmethod
    def encode(message : str) -> list:
        '''Encode a message from text to plaintext

        Input:
            - message : str
        
        Output:
            - list of integer plaintext
        '''
        return [ord(c) for c in message]

    @staticmethod
    def decode(plain : list) -> str:
        '''Convert plaintext to message

        Input:
            - plain : plaintext in string
        
        Output:
            - message string.
        '''
        return ''.join([chr(c) for c in plain])
