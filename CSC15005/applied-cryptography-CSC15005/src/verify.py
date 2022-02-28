from RSA import RSA
import sys, getopt, hashlib

BUFFER_SIZE = 64 * 1024 # 64kb

def main(argv):
    input_file, input_signature = '', ''
    public, n = None, None

    try:
        opts, _ = getopt.getopt(argv, 'hi:o', ['input_file=', 'input_signature=', 'public=', 'n='])
    except getopt.GetoptError:
        print('Command line arguments invalid, try again.')
        sys.exit(2)
    
    for opt, arg in opts:
        if opt == '--input_file':
            input_file = arg
        if opt == '--input_signature':
            input_signature = arg
        if opt == '--public':
            public = int(arg)
        if opt == '--n':
            n = int(arg)
    
    if input_file == '' or input_signature == '':
        print('Missing input file / signature file.')
        sys.exit(2)
    
    if public is None or n is None:
        print('Missing public / n')
        sys.exit(2)
    
    # Create file digest (hash)
    file_digest = hashlib.sha256()
    with open(input_file, 'rb+') as f:
        # Creating hash by reading file into chunks
        while True:
            data = f.read(BUFFER_SIZE)
            if not data: break

            file_digest.update(data)

    # File digest decrypted from signature
    with open(input_signature, 'r+') as f:
        file_signature = f.read()
    
    file_digest_check = RSA.decrypt(file_signature, public, n)

    print('File digest: {0}'.format(file_digest.hexdigest()))
    print('File original digest: {0}'.format(file_digest_check))

    if file_digest.hexdigest() == file_digest_check:
        print('This file is authorised by the author - signature valid.')
    else:
        print('This file is not authorised by the author - file has been modified.')
    
if __name__ == '__main__':
    main(sys.argv[1:])