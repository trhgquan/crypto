from symmetric import SymmetricDH
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

    p, g, ka, kb, x, y  = SymmetricDH.generate_key(p)
    print('Generated: p = {0}, g = {1}, ka = {2}, kb = {3}, x = {4}, y = {5}'.format(
        p, g, ka, kb, x, y
    ))

if __name__ == '__main__':
    main(sys.argv[1:])