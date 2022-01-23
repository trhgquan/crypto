from RSA import RSA
import sys, getopt

def main(argv):
    input_file, output_file = '', ''
    n, e = None, None

    try:
        opts, _ = getopt.getopt(argv, 'hi:o', ['input=', 'output=', 'n=', 'e='])
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
        if opt == '--e':
            e = int(arg)

    if input_file == '' or output_file == '':
        print('Missing input / output')
        sys.exit(2)
    
    if n is None or e is None:
        print('Missing n / e')
        sys.exit(2)

    cipher = ''
    with open(input_file, 'r+') as f:
        message = f.read()
        for c in RSA.encrypt(message, e, n):
            cipher += str(c)
            cipher += ' '
    
    with open(output_file, 'w+') as f:
        print(cipher, file = f)
        print('Result are in {0}'.format(output_file))

if __name__ == '__main__':
    main(sys.argv[1:])