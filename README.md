# Crypto
Cài đặt thuật & tóm tắt lí thuyết các môn học
- CSC15005: Nhập môn mã hóa - mật mã
- CSC15003: Mã hóa ứng dụng

[Xem repository của site trên GitHub](https://github.com/trhgquan/crypto)

## Chủ đề
### CSC15005 - Nhập môn mã hóa - mật mã
#### [CSC15005/RSA](CSC15005/RSA).
- Bàn về Hệ mã bất đối xứng RSA (Rivest - Shamir - Adleman).
- Extended Euclidean Algorithm (Thuật toán Euclidean mở rộng - XEuclidean).
- Chinese Remainder Theorem.
- Sinh số nguyên lớn.

#### [CSC15005/DLP-based cryptosystems](CSC15005/DLP-based).
- Bàn về lý thuyết nhóm (Group Theory).
- Bàn về Hệ mã đối xứng Diffie-Hellman.
- Bàn về Hệ mã bất đối xứng El-Gamal.
- Bàn về phương pháp giải bài toán DLP (Discrete Logarithm Problem - Bài toán Logarithm rời rạc) sử dụng thuật toán Index Calculus và số B-smooth.
- Giới thiệu sơ nét về ECC (Elliptic Curve Cryptosystems - Hệ mã đường cong Elliptic).

#### [CSC15005/Symmetric cryptosystems](CSC15005/symmetric-crypto).
- Các mode của symmetric crypto.
- Matrix cipher (Mã Ma trận, ví dụ với Hill Cipher).

#### [CSC15005/Applied cryptography](CSC15005/applied-cryptography/).
- Hash function (Hàm băm mật mã).
- Chữ ký điện tử (Sử dụng RSA).
- Zero-knowledge (Tri thức trị không)
- Hệ bảo mật thông tin - Bảo mật cơ sở dữ liệu.
- Chia sẻ bí mật: đa thức nội suy Lagrange, bài toán ngưỡng.

### CSC15003 - Mã hóa ứng dụng

#### [CSC15003/cryptosystem](CSC15003/cryptosystem)
- Giới thiệu sơ nét về hệ thống mã hóa
- So sánh hệ mã đối xứng (symmetric cryptosystem) và bất đối xứng (asymmetric cryptosystem).
- Giới thiệu sơ nét vành $Z_m$

#### [CSC15003/symmetric-cryptosystem](CSC15003/symmetric-cryptosystem)
- Bàn về các phương pháp mã hóa đối xứng tiêu biểu.

#### [CSC15003/shannon-theory](CSC15003/shannon-theory)
- Bàn sơ lược về Lý thuyết Shannon.

#### [CSC15003/modes-of-operation](CSC15003/modes-of-operation)
- Các modes hoạt động của mã hóa đối xứng.

#### [CSC15003/digital-signature](CSC15003/digital-signature)
- Bàn sơ lược về chữ ký số.

#### [CSC15003/hash-function](CSC15003/hash-function)
- Bàn sơ lược về hàm băm (hash function).

#### [CSC15003/certificate-and-ssl](CSC15003/certificate-and-ssl)
- Bàn sơ về certificate và SSL.

## Tài nguyên bổ trợ
- [Source code CSC15003](https://github.com/trhgquan/CS153) - cài đặt bằng C++.
    - BigInt.
    - AES KeyExpansion.
    - PrimeCheck sử dụng Thuật toán Miller-Rabin.
    - MD5.

- [Source code CSC15005](https://github.com/trhgquan/CS155) - cài đặt bằng Python.
    - Symmetric Crypto: Matrix Cipher.
    - Asymmetric Crypto: RSA, ElGamal.
    - DLP: Diffie-Hellman (symmetric), ElGamal (asymmetric).
    - Digital Signature: DSA.

- [Đồ án cuối kỳ CSC15005](https://github.com/trhgquan/image-sharing).
    - Cài đặt hệ thống chia sẻ ảnh an toàn, yêu cầu ảnh phải được mã hóa khi lưu trữ trên server.

## LICENSE
This project is licensed under the terms of [The GNU GPL v3.0 License](LICENSE)

VNUHCM - US, Mùa Thu năm 2021 (CSC15005) - Mùa Xuân 2022 (CSC15003).
