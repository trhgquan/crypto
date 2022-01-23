from elgamal import Elgamal
import sys, getopt

def main(argv):
    input_file, output_file = '', ''
    d, p = None, None

    try:
        opts, _ = getopt.getopt(argv, 'hi:o', ['input=', 'output=', 'd=', 'p='])
    except getopt.GetoptError:
        print('Command line arguments invalid, try again.')
        sys.exit(2)
    
    for opt, arg in opts:
        if opt == '--input':
            input_file = arg
        if opt == '--output':
            output_file = arg
        if opt == '--d':
            d = int(arg)
        if opt == '--p':
            p = int(arg)

    if input_file == '' or output_file == '':
        print('Missing input / output')
        sys.exit(2)
    
    if d is None or p is None :
        print('Missing d / p')
        sys.exit(2)
    
    with open(input_file, 'r+') as f:
        c1 = int(f.readline())
        c2 = f.readline()
    
    with open(output_file, 'w+') as f:
        print(Elgamal.decrypt(d, c1, c2, p), file = f)
    
    print('Result are in {0}'.format(output_file))

if __name__ == '__main__':
    main(sys.argv[1:])