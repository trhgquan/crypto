from RSA import RSA
import sys, getopt, hashlib

BUFFER_SIZE = 64 * 1024 # 64kb

def main(argv):
    input_file, output_file = '', ''
    secret, n = None, None

    try:
        opts, _ = getopt.getopt(argv, 'hi:o', ['input=', 'output=', 'secret=', 'n='])
    except getopt.GetoptError:
        print('Command line arguments invalid, try again.')
        sys.exit(2)
    
    for opt, arg in opts:
        if opt == '--input':
            input_file = arg
        if opt == '--output':
            output_file = arg
        if opt == '--secret':
            secret = int(arg)
        if opt == '--n':
            n = int(arg)
    
    if input_file == '' or output_file == '':
        print('Missing input / output file.')
        sys.exit(2)
    
    if secret is None or n is None:
        print('Missing secret / n')
        sys.exit(2)
    
    # Create file digest (hash)
    file_digest = hashlib.sha256()
    with open(input_file, 'rb+') as f:
        # Creating hash by reading file into chunks
        while True:
            data = f.read(BUFFER_SIZE)
            if not data: break

            file_digest.update(data)
    
    file_digest_str = file_digest.hexdigest()
    file_signature = ''
    for c in RSA.encrypt(file_digest_str, secret, n):
        file_signature += str(c)
        file_signature += ' '

    with open(output_file, 'w+') as f:
        print(file_signature, file = f)

    print('Filename: {0}'.format(input_file))
    print('File digest: {0}'.format(file_digest_str))
    print('File signature: {0}'.format(file_signature))
    print('Signature stored inside {0}'.format(output_file))

if __name__ == '__main__':
    main(sys.argv[1:])