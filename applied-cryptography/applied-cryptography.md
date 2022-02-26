# Mã hóa ứng dụng
## 1. Hàm băm (Hash function)
### Định nghĩa
Hàm hash $h$ biến doc thành signature $\in \mathbb{Z}_{2^l}$ ($l$ bit).

$h: \{0, 1\}^{*} \rightarrow \{0, 1\}^l$ thỏa
1. Cho $y = h(m) \rightarrow$ tìm $m$ khó. (tính 1 chiều)
2. Cho $m$, tìm $m'$ sao cho $h(m) = h(m')$ khó. 
3. Tìm $m, m'$ sao cho $h(m) = h(m')$ khó.

Trường hợp 2 và 3: hạn chế đụng độ

### Cài đặt
Cách 1: Dùng hệ mã $E$ (AES, 3DES, RSA, ..)

Cách 2: Kết hợp băm
VD: $h_1, h_2$ là 2 hàm băm $\rightarrow h_1 \oplus h_2, h_2 \oplus h_1$

Cách 3: Xây dựng thuật giải

VD: MASH: $\{0, 1\}^{*}\rightarrow \{0, 1\}^{n/2}$
1. Chọn $p, q$ nguyên tố, $M = pq$ có $m$ bit.
2. Chọn $n$ là bội của 16 sao cho $n < m$.
3. $H_0 = 0, A = 1111 0000 ... 0000$ ($n$ bit)
4. $X$ là thông điệp.
- Chia $X$ thành $t$ khối $\frac{n}{2}$ bit.
- Thêm $\frac{n}{2}$ bit là giá trị b (giá trị của chiều dài $x$).
5. Lặp từ $i = 1 \rightarrow t$:
- Chia khối $X_i$ thành các khối 4 bit.
- Chèn 4 bit 1111 vào trước, riêng khối cuối chèn $1010$.

Kết quả là $Y = y_1..y_t$

6. Lặp từ $i = 1 \rightarrow t$:
- $F_i = (H_{i - 1} \oplus y_i \lor A)^{257} \pmod M$
- Lấy $G_i$ là $n$ bit phải $F_i$.
- Tính $H_i = (a_i \oplus H_{i - 1})$
7. $H_t$ là kết quả.

### Popular cryptographic hash functions:
- MD5 (mostly in password hashing)
- SHA-* (1 - 128bit, 2 - 256bit, 3 - non limited; mostly in blockchain SHA2)

### Ứng dụng:
1. Bảo mật passwords
- Bảo vệ đường truyền: RSA - mã hóa username và password
- Bảo vệ dữ liệu trong database: hash password

2. Mã chứng thực văn bản (MAC - Message Authentication Code)
- Bảo vệ tính toàn vẹn của văn bản.
    - VD: Cho document $M, c = h(M || k)$ (ghép $k$ là khóa bí mật của người chủ văn bản vào $M$)

3. Chữ ký điện tử (Digital Signature)
Văn bản gốc $M$, $C$ có $e, d$ (RSA), $A$ có khóa $k$ bí mật.

- Với $A$: tạo mã chứng thực $a = MAC(M || k)$.
- Với $C$: 
    - Nén M thành u: $u = h(M)$.
    - Chữ ký của người công chứng: $s = RSA(d, u)$
- Mọi người đều có thể kiểm tra: so sánh $h(M) = RSA(e, s)$ 

### Phân tích hàm băm mật mã
Cho $P$, tìm đụng độ $P'$:
1. Tạo bảng $t = 2^{\frac{n}{2}}$ biến thể của $P: P_1, P_2, ..$
2. Lặp: $\forall i \in t:$ chèn $(P_i, h(P_i))$ vào $t$.
3. Tạo $P'$, tra trong $t$.

Kháng: cho $n \geq 80k, (k > 1)$

## 2. Chữ ký điện tử
**Nguyên lí chung**: dựa trên hệ mã public key cryptosystem $f$.
- $s = f_d(m)$, chỉ có chủ giữ $d$ mới ký được
- Mọi người đều có $e$, nên đều có thể kiểm tra $f^{-1}_e(s) = m$

Tuy nhiên $f$ ký rất chậm trên $m$. Thay vì vậy người ta ký trên hash $h(m)$, với $h$ là hàm băm mật mã.

### Naive version, using RSA:
Tạo key:
- Sử dụng pha tạo key của RSA tạo $n, e, d$. Chú ý $e$ dùng để ký - bí mật, $d$ dùng để kiểm chứng - công khai.

Pha ký:
- Người ký tạo digest $h$ từ document $m$, sau đó dùng RSA mã hóa $h$ thành chữ ký $s$ bằng khóa bí mật $e$.
- Người ký công khai document $m$, chữ ký $s$ và $n, d$.

Pha kiểm chứng:    
- Người kiểm chứng tạo digest $h$ từ document $m$.
- Người kiểm chứng giải mã $s$ thành $h'$, dùng $d, n$ với thuật toán RSA
- Nếu $h' = h$, document $m$ được gửi đi toàn vẹn, không bị chỉnh sửa, đúng người ký.

Cài đặt trong thư mục `src`.

### DSA (Digital Signature Algorithm) - DSS (Digital Signature Standard)
**Quan trọng**: Ký cần nhanh, verify không cần nhanh. Giải mã nhanh có cách (CRT).

1. Các tham số:
    - p là số nguyên tố (khoảng 512 bit).
    - q là số nguyên tố (khoảng 160 bit).
    - $g \in \mathbb{Z}_N$ (bậc $g$ là bội của $q$)
    - $h: \{0, 1\}^{*} \rightarrow \{0, 1\}^{160}$
    - $x : 0 < x < q$ (khóa mật)
    - $y \equiv g^x \pmod p$ (Diffie-Hellman - khóa công khai)
2. Ký văn bản $m$:
    - Chọn ngẫu nhiên $k \in \mathbb{Z}_N$
    - $r \equiv (g^k \pmod p) \pmod q, s \equiv k^{-1}(h(m) + xr) \pmod q$ (Ký bằng khóa $x$)
    - Kết quả là $(r, s)$.
3. Xác minh chữ ký:
    - $t \equiv s^{-1} \pmod p$
    - $r \equiv (g^{h(m)t}y^{rt} \pmod p) \pmod q$ (Kiểm bằng khóa $y$)



## 3. Zero-knowledge - tri thức trị không
$A$ sử dụng khóa công khai $\pmod n$, $n = pq, p, q$ là số nguyên tố, $p, q \equiv 3 \pmod 4$.

$A$ thuyết phục người $B$ về khóa công khai là của mình:

1. $A$ làm:
    - Chọn một $s$ là số chính phương $\pmod n$, công bố $(n, s)$
    - Tính $t^2 \equiv s \pmod n$ và giữ bí mật $t$.
2. $A$ làm:
    - Chọn ngẫu nhiên $r < n$
    - $z_1 \equiv r^2 \pmod n, z_2 \equiv sz_1^{-1} \pmod n$
    - Gửi $(z_1, z_2)$ cho $B$.
3. $B$ làm:
    - Kiểm $s \equiv z_1z_2 \pmod n$
    - Chọn 1 bit $c \in \{0, 1\}$ 
    - Gửi $c$ cho $A$.
4. $A$ làm:
    - $c = 0$ thì gửi $r$.
    - $c = 1$ thì gửi $t^{r - 1}$.
5. $B$ làm:
    - $c = 0$ thì kiểm $r^2 \equiv z_1 \pmod n$.
    - $c = 1$ thì kiểm $(t^{r - 1})^2 \equiv z_2 \pmod n$.

Cách trên là Interactive Proving.

# 4. Hệ bảo mật thông tin

## Bảo mật CSDL
Không giống CSDL quan hệ thường học, CSDL có thể là file, record, row, col, ..

Xét CSDL $D = \{f_1, f_2, .., f_n\}$ - plain. Ta muốn mã hóa $D$ thành $C$

### Pha 1: Mã hóa CSDL
Sử dụng CRT để mã hóa CSDL.

1. Sinh $n$ số nguyên tố $p_i$ khác nhau thỏa $p_i > f_i \forall i \in [1, n]$
2. Giải hệ
    - $X \equiv f_1 \pmod{p_1}$
    - ...
    - $X \equiv f_n \pmod{p_n}$
3. $C = X$ là mã hóa của $D$, $p_i$ là khóa để đọc $f_i$, gửi khóa $p_i$ này cho chủ của $f_i$

### Pha 2: $u_i$ đọc $f_i$
4. $f_i \equiv C \pmod{p_i}$


## 5. Chia sẻ bí mật
### a. Đa thức nội suy Lagrange.
#### Định nghĩa
Đa thức $P_n(x)$ bậc $n$ được sinh bởi $n$ cặp $(x_i, y_i)$. Khi đó

$\displaystyle P_n(x) = \sum_{j = 1}^{n} y_j L_j(x)$

Với $\displaystyle L_j(x) = \prod_{1 \leq m \leq n, m \neq j} \frac{x - x_m}{x_j - x_m}$

#### Ví dụ: 
- với $n = 2$, đa thức $\displaystyle P_2(x) = y_1\frac{x - x_2}{x_1 - x_2} + y_2\frac{x - x_1}{x_2 - x_1}$
- với $n = 3$, đa thức $\displaystyle P_3(x) = y_1\frac{(x - x_2)(x - x_3)}{(x_1 - x_2)(x_1 - x_3)} + y_2\frac{(x - x_1)(x - x_3)}{(x_2 - x_1)(x_2 - x_3)} + y_3\frac{(x - x_1)(x - x_2)}{(x_3 - x_1)(x_3 - x_2)}$

### b. Ứng dụng: bài toán ngưỡng
Ví dụ: với ngưỡng $n = 3$ và $N = 5$ người, hàm $P_3(x) = ax^2 + bx + c$. Khi đó $c$ là bí mật cần phải có 3 người cùng mở khóa mới có thể giải mã.

Ở đây ta chọn $a = 5, b = 6, c = 4$, các phép toán thực hiện trong $\mathbb{Z}_7$. Hàm $P(x) = 5x^2 + 6x + 4$. Nên nhớ bước này hoàn toàn do người chọn, $a, b$ được giữ bí mật và $c$ là bí mật được chia sẻ. Ta cũng quy định mỗi người có cặp $(i, P(i))$ là khóa. Vậy 5 người lần lượt có các khóa $u_1 = (1, 1), u_2 = (2, 1), u_3 = (3, 4), u_4 = (4, 3), u_5 = (5, 5)$.

Khi đó, nếu cần biết $c$ thì cần 3 người dùng khóa của mình để mở. Khi đó ta tính $P(0)$ với các $x_1, x_2, x_3, y_1, y_2, y_3$ từ khóa của người dùng.

Ví dụ:
- Nếu $u_1, u_2, u_3$ cùng nhau giải mã, khi đó $\displaystyle P(0) = 1\frac{(0 - 2)(0 - 3)}{(1 - 2)(1 - 3)} + 1\frac{(0 - 1)(0 - 3)}{(2 - 1)(2 - 3)} + 4\frac{(0 - 1)(0 - 2)}{(3 - 1)(3 - 2)} = 4$
- Tương tự, chỉ cần 3 người cùng nhau giải mã sẽ thu được $c$.
