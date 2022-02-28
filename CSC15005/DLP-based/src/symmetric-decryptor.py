from symmetric import SymmetricDH
import sys, getopt

def main(argv):
    input_file, output_file = '', ''
    p, k, x = None, None, None

    print('Note: ka-y, kb-x, use any of them')

    try:
        opts, _ = getopt.getopt(argv, 'hi:o', ['input=', 'output=', 'p=', 'k=', 'x='])
    except getopt.GetoptError:
        print('Command line arguments invalid, try again.')
        sys.exit(2)
    
    for opt, arg in opts:
        if opt == '--input':
            input_file = arg
        if opt == '--output':
            output_file = arg
        if opt == '--p':
            p = int(arg)
        if opt == '--k':
            k = int(arg)
        if opt == '--x':
            x = int(arg)

    if input_file == '' or output_file == '':
        print('Missing input / output')
        sys.exit(2)
    
    if p is None or k is None or x is None :
        print('Missing p / k / x')
        sys.exit(2)
    
    with open(input_file, 'r+') as f:
        cipher = f.read()
    
    with open(output_file, 'w+') as f:
        print(SymmetricDH.decrypt_xor(cipher, k, x, p), file = f)

    print('Result are in {0}'.format(output_file))

if __name__ == '__main__':
    main(sys.argv[1:])