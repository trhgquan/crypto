# Hệ mã đối xứng

## 1. Tóm tắt
Với $\mathbb{M}, \mathbb{C}, \mathbb{K}$ lần lượt là không gian tin, không gian mã và không gian khóa

$E_k : \mathbb{M} \rightarrow \mathbb{C}$ khả nghịch $(E^{-1} \equiv D)$

$\forall m \in \mathbb{M}: D(E(m)) = m$ với $E(m) \in C$

$E: \mathbb{M} \times \mathbb{K} \rightarrow \mathbb{C} : D(E(m, k), k) = m\ \forall m \in \mathbb{M}, k \in \mathbb{K}$

## 2. Một phương pháp mã hóa đối xứng (Diffie-Hellman)
- Pha mã hóa: $c = m \oplus k$ (phép $\oplus$ là phép XOR)
- Pha giải mã: $m = c \oplus k$

**Chú ý** là làm cách này không cần tìm $k^{-1}$ và $\pmod p$.


```python
c, m, k = 6, 9, 11

c1 = m ^ k
m1 = c1 ^ k

print(m, m1)
```

    9 9
    

## 3. Dạng mã
$\text{Doc} = m_1m_2..m_n$, $\text{len}(m_i) = l$ bit

- Đơn vị của $l =$ unit (bit) => **Stream** cipher (mã **dòng**)
- Đơn vị của $l \neq$ unit (bit) => Block cipher (mã khối)

## 4. Modes

### a. Electronic Codebook (ECB) - từ điển
- $c_i \equiv E(m_i, k)$

### b. Cipher block chaining (CBC) - xích
- $c_0 =$ i.v (initial value, cho đại)
- $c_1 = E(m_1, k) \oplus c_0$
- ...
- $c_i = E(m_i, k) \oplus c_{i - 1} (1 \leq i \leq n)$

Giải mã: làm ngược lại
- $m_i = D(m_i, k) \oplus c_{i - 1}$

### c. Propagating CBC (PCBC)
- $c_0 = \text{i.v}$ (initial value, cho đại)
- $c_i = E(m_i \oplus c_{i - 1} \oplus m_{i - 1}, k)$

### d. Cipher feedback (CFB)
- $c_0 = \text{i.v}$ (initial value, cho đại)
- $c_i = m_i \oplus E(c_{i - 1}, k)$

### e. Output feedback (OFB)
(mã hóa key)
- $y_0 = E(\text{iv}, k)$
- $c_i = m_i \oplus E(y_{i - 1}, k)$

### f. Counter (CTR)
- iv = token
- $c_i = m_i \oplus E(\text{iv} + g(i), k)$
- $g(i)$ là biến đếm

## Nguyên tắc thiết kế hàm mã

- (R1) Thay thế: $b_0..b_l \xrightarrow{\text{sub (thay thế)}}b'_0..b'_l$
- (R2) Hoán vị: $b_0..b_l \xrightarrow{\text{per (hoán vị)}}b'_0..b'_l: b_i = b'_{\sigma(i)}$

## Matrix Cipher
### Hill Cipher

Cho $A_{n\times n}$ là ma trận khả nghịch $n$ dòng, $n$ cột. Với mẩu tin kích thước $M_{n\times 1}$, ta có:
- hàm mã hóa $E(M, A) = AM \pmod p$
- hàm giải mã $D(M, A) = A^{-1}M \pmod p$

**Chú ý**: Ma trận $A^{-1}$ là nghịch đảo của $A$ trong $\mathbb{Z}_p$. Trong $\mathbb{Z}_p$ chỉ có phép **cộng** và **nhân**, còn phép chia phải tìm modulo nghịch đảo!

## Tạo nhanh ma trận khả nghịch (keygen)
- Mệnh đề 1: Ma trận khả nghịch khi định thức khác 0.
- Mệnh đề 2: Định thức ma trận tam giác trên (upper-triangular matrix) và định thức ma trận tam giác dưới (lower-triangular matrix) bằng tích các phần tử trên đường chéo.
- Mệnh đề 3: $det(AB) = det(A)det(B)$

1. Tạo $U, L$ lần lượt là 2 ma trận tam giác trên và tam giác dưới có định thức khác 0.
2. Khóa $K = LU$.
3. Vì bản thân $K$ khả nghịch, nên $KK^{-1} = I_n$ Ta giải hệ sau:
- $LY = E$ ($E$ là ma trận đơn vị)
- $UX = Y$

khi đó $X$ là nghịch đảo của $K$.

Đây chỉ là tóm tắt, bản thân mỗi phần nhân ma trận lại có cách làm nhanh. Xem chi tiết trong phần src.
