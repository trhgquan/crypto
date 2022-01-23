from elgamal import Elgamal
import sys, getopt

def main(argv):
    p = None

    try:
        opts, _ = getopt.getopt(argv, 'hi:o', ['p='])
    except getopt.GetoptError:
        print('Command line arguments invalid, try again.')
        sys.exit(2)
    
    for opt, arg in opts:
        if opt == '--p':
            p = int(arg)

    if p is None:
        print('Missing p.')
        sys.exit(2)

    p, g, d, e = Elgamal.generate_key(p)
    print('Generated: p = {0}, g = {1}, d = {2}, e = {3}'.format(p, g, d, e))

if __name__ == '__main__':
    main(sys.argv[1:])