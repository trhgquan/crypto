from elgamal import Elgamal
import sys, getopt

def main(argv):
    input_file, output_file = '', ''
    e, p, g = None, None, None

    try:
        opts, _ = getopt.getopt(argv, 'hi:o', ['input=', 'output=', 'e=', 'p=', 'g='])
    except getopt.GetoptError:
        print('Command line arguments invalid, try again.')
        sys.exit(2)
    
    for opt, arg in opts:
        if opt == '--input':
            input_file = arg
        if opt == '--output':
            output_file = arg
        if opt == '--e':
            e = int(arg)
        if opt == '--p':
            p = int(arg)
        if opt == '--g':
            g = int(arg)

    if input_file == '' or output_file == '':
        print('Missing input / output')
        sys.exit(2)
    
    if e is None or p is None or g is None:
        print('Missing e / p / g')
        sys.exit(2)
    
    with open(input_file, 'r+') as f:
        message = f.read()
        
    encrypted_content = Elgamal.encrypt(message, e, p, g)
    with open(output_file, 'w+') as f:
        print(encrypted_content[0], file = f)
        print(*encrypted_content[1], sep = ' ', file = f)
    
    print('Result are in {0}'.format(output_file))

if __name__ == '__main__':
    main(sys.argv[1:])