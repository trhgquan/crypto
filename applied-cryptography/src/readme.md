# Demo RSA Digital Signature (naive version)
## Installation
```
pip install -r requirementst.txt
```

### Key generator
Same as RSA keygen:
```
python generator.py --p=<first prime> --q=<second prime>
```

### Sign
```
python sign.py --input=<file to sign> --output=<file to store signature> --secret=<signing key (private key)> --n=<RSA n>
```

Example:
```console
python sign.py --input=requirements.txt --secret=8907673 --n=68449547 --output=signature.txt
Filename: requirements.txt
File digest: 7eb70257593da06f682a3ddda54a9d260d4fc514f645237f5ca74b08f8da61a6
File signature: 29313164 2202787 11841552 29313164 15971020 29055442 9207571 29313164 9207571 52999540 40371090 61999174 35108868 15971020 68404682 5397042 68404682 4297162 29055442 35108868 40371090 61999174 61999174 61999174 35108868 9207571 54455790 35108868 52999540 61999174 29055442 68404682 
15971020 61999174 54455790 5397042 27702381 9207571 44953044 54455790 5397042 68404682 54455790 9207571 29055442 40371090 29313164 5397042 9207571 27702381 35108868 29313164 54455790 11841552 15971020 4297162 5397042 4297162 61999174 35108868 68404682 44953044 35108868 68404682
Signature stored inside signature.txt
```

## Verify
```
python verify.py --input_file=<file to verify> --input_signature=<signature file> --public=<verify (public) key> --n=<RSA n>
```

Example:
```console
python verify.py --input_file=requirements.txt --input_signature=signature.txt --public=10007977 --n=68449547    
File digest: 7eb70257593da06f682a3ddda54a9d260d4fc514f645237f5ca74b08f8da61a6
File original digest: 7eb70257593da06f682a3ddda54a9d260d4fc514f645237f5ca74b08f8da61a6
This file is authorised by the author - signature valid.
```