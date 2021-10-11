from bigmod import BigMod

class GroupGenerator:
    def __init__(self, n):
        self.__n = n

    def naive_list(self):
        for i in range(2, self.__n):
            is_generator = True
            power = 1
            generated = []
            while 1:
                m = BigMod().power(i, power, self.__n)
                if (m not in generated):
                    generated.append(m)
                else: break
                power += 1

            if len(generated) != self.__n - 1: is_generator = False

            if is_generator: print(i)


def main():
    n = int(input('n = '))
    GroupGenerator(n).naive_list()

if __name__ == '__main__':
    main()
