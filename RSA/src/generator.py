from RSA import RSA
import sys, getopt

def main(argv):
    p, q = None, None

    try:
        opts, _ = getopt.getopt(argv, 'hi:o', ['p=', 'q='])
    except getopt.GetoptError:
        print('Command line arguments invalid, try again.')
        sys.exit(2)
    
    for opt, arg in opts:
        if opt == '--p':
            p = int(arg)
        if opt == '--q':
            q = int(arg)

    if p is None or q is None:
        print('Missing p / q')
        sys.exit(2)

    n, e, d = RSA.generate(p, q)
    print('Generated n = {0}, e = {1}, d = {2}'.format(n, e, d))

if __name__ == '__main__':
    main(sys.argv[1:])