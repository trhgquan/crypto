from RSA import RSA
import sys, getopt

def main(argv):
    input_file, output_file = '', ''
    n, d = None, None

    try:
        opts, _ = getopt.getopt(argv, 'hi:o', ['input=', 'output=', 'n=', 'd='])
    except getopt.GetoptError:
        print('Command line arguments invalid, try again.')
        sys.exit(2)
    
    for opt, arg in opts:
        if opt == '--input':
            input_file = arg
        if opt == '--output':
            output_file = arg
        if opt == '--n':
            n = int(arg)
        if opt == '--d':
            d = int(arg)

    if input_file == '' or output_file == '':
        print('Missing input / output')
        sys.exit(2)
    
    if n is None or d is None:
        print('Missing n / d')
        sys.exit(2)

    with open(input_file, 'r+') as f:
        cipher = f.read()
    
    with open(output_file, 'w+') as f:
        print(RSA.decrypt(cipher, d, n), file = f)
        print('Result are in {0}'.format(output_file))

if __name__ == '__main__':
    main(sys.argv[1:])