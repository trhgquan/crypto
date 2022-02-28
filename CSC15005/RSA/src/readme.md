# Demo RSA source code
## Installation
```
pip install -r requirements.txt
```

## Generator
Generate a pair of (n, e, d):
```
python generator.py --p=<first prime> --q=<second prime>
```

Example:
```console
python generator.py --p=131 --q=199
Generated n = 26069, e = 3287, d = 12083
```

## Encryptor
Encrypt a file (text only)
```
python encryptor.py --input=<input file> --output=<encrypted file> --n=<RSA n> --e=<RSA public (encryption) key>
```

Example:
```console
python encryptor.py --input=test.txt --output=encrypted.txt --n=26069 --e=3287
Result are in encrypted.txt
```

## Decryptor
Decrypt a file
```
python encryptor.py --input=<encrypted file> --output=<decrypted file> --n=<RSA n> --d=<RSA private (decryption) key>
```

Example:
```console
python decryptor.py --n=26069 --d=12083 --input=encrypted.txt --output=decrypted.txt
Result are in decrypted.txt
```

## Prime generator
Usage:
```
PrimeGen(seed = <prime seed>).create(<expected length>)
```