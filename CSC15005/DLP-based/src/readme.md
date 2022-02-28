# Demo DLP-based source code
## Installation
```
pip install -r requirementst.txt
```

## Symmetric
### Key generator
```
python symmetric-generator.py --p=<prime>
```

Example:
```console
python symmetric-generator.py --p=269
Generated: p = 269, g = 240, ka = 220, kb = 72, x = 160, y = 257
```

### Encryptor
```
python symmetric-encryptor.py --input=<input file> --output=<output file> --p=<prime> --k=<key> --x=<power>
```

Example:
```console
python symmetric-encryptor.py --p=269 --k=220 --x=257 --input=test.txt --output=encrypted.txt
Note: ka-y, kb-x, use any of them
Result are in encrypted.txt
```

### Decryptor
```
python symmetric-decryptor.py --input=<input file> --output=<output file> --p=<prime> --k=<key> --x=<power>
```

Example:
```console
python symmetric-decryptor.py --p=269 --k=72 --x=160 --input=encrypted.txt --output=decrypted.txt
Note: ka-y, kb-x, use any of them
Result are in decrypted.txt
```

## ElGamal
### Key generator
```
python elgamal-generator.py --p=<prime>
```

Example:
```console
python elgamal-generator.py --p=269
Generated: p = 269, g = 8, d = 245, e = 155
```

### Encryptor
```
python elgamal-encryptor.py --p=<prime> --g=<group generator> --e=<encryption key> --input=<input file> --output=<output file>
```

Example:
```console
python elgamal-encryptor.py --p=269 --g=8 --e=155 --input=test.txt --output=encrypted.txt
Result are in encrypted.txt
```

### Decryptor
```
python elgamal-decryptor.py --p=<prime> --d=<decryption key> --input=<input file> --output=<output file>
```

Example:
```console
python elgamal-decryptor.py --input=encrypted.txt --output=decrypted.txt --d=245 --p=269
Result are in decrypted.txt
```