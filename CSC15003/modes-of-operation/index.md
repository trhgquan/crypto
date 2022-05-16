## Modes of Operation

Kết hợp mode + thuật toán = encryption scheme

### Electronic Codebook (ECB)
Chia message thành từng đoạn, mỗi đoạn mã hóa độc lập

### Cipher-block chaining (CBC)
1 khối plaintext được XOR với ciphertext trước khi mã.

- $C_0 = \texttt{IV}$
- $C_i = E_K(P_i \oplus C_{i - 1})$

### Propagating CBC (PCBC)
Xài $P_{i - 1}$ và $P_i$

### Cipher feedback (CFB)
Plaintext XOR với output trước.

- $C_0 = \texttt{IV}$
- $C_i = P_i \oplus E_K(C_{i - 1})$

Dùng thuật encrypt cho giải mã.

### Output feedback (OFB)
- $O_0 = \texttt{IV}$
- $O_i = E_K(O_{i - 1})$
- $C_i = P_i \oplus O_i$

### Counter (CTR)
Tự xem lại CSC15005

## Lan truyền lỗi

Tự xem lại, chủ yếu các mode nào có link với nhau thì sẽ có hiện tượng lan truyền lỗi. Nhưng tùy vào cái cách nó link mà lỗi nhiều hay ít.

## Padding Scheme
aka thêm cho đủ byte / bit

Các phương pháp cơ bản:
- Bit padding
- Byte padding

I.e: 
- 1 block 16 byte, kích thước block ban đầu 15 bytes -> chèn thêm 1 bytes
- 1 block 16 byte, kích thước block ban đầu 16 bytes -> vẫn phải chèn thêm 16 bytes.
