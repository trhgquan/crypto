# Mã hóa ứng dụng
## 1. Hàm băm (Hash function)
### Định nghĩa
Hàm hash <span>$h$ biến doc thành signature $\in \mathbb{Z}_{2^l}$ ($l$</span> bit).

1. Cho <span>$y = h(m) \rightarrow$ tìm $m$</span> khó. (tính 1 chiều)
2. Cho <span>$m$, tìm $m'$ sao cho $h(m) = h(m')$</span> khó. 
3. Tìm <span>$m, m'$ sao cho $h(m) = h(m')$</span> khó.

Trường hợp 2 và 3: hạn chế đụng độ

### Cài đặt
Cách 1: Dùng hệ mã <span>$E$</span> (AES, 3DES, RSA, ..)

Cách 2: Kết hợp băm
VD: <span>$h_1, h_2$ là 2 hàm băm $\rightarrow h_1 \oplus h_2, h_2 \oplus h_1$</span>

Cách 3: Xây dựng thuật giải

VD: MASH: <span>$\{0, 1\}^{*}\rightarrow \{0, 1\}^{n/2}$</span>
1. Chọn <span>$p, q$ nguyên tố, $M = pq$ có $m$</span> bit.
2. Chọn <span>$n$ là bội của 16 sao cho $n < m$</span>.
3. <span>$H_0 = 0, A = 1111 0000 ... 0000$ ($n$</span> bit)
4. <span>$X$</span> là thông điệp.
- Chia <span>$X$ thành $t$ khối $\frac{n}{2}$</span> bit.
- Thêm <span>$\frac{n}{2}$ bit là giá trị b (giá trị của chiều dài $x$</span>).
5. Lặp từ <span>$i = 1 \rightarrow t$</span>:
- Chia khối <span>$X_i$</span> thành các khối 4 bit.
- Chèn 4 bit 1111 vào trước, riêng khối cuối chèn <span>$1010$</span>.

Kết quả là <span>$Y = y_1..y_t$</span>

6. Lặp từ <span>$i = 1 \rightarrow t$</span>:
- <span>$F_i = (H_{i - 1} \oplus y_i \lor A)^{257} \pmod M$</span>
- Lấy <span>$G_i$ là $n$ bit phải $F_i$</span>.
- Tính <span>$H_i = (a_i \oplus H_{i - 1})$</span>
7. <span>$H_t$</span> là kết quả.

### Popular cryptographic hash functions:
- MD5 (mostly in password hashing)
- SHA-* (1 - 128bit, 2 - 256bit, 3 - non limited; mostly in blockchain SHA2)

### Ứng dụng:
1. Bảo mật passwords
- Bảo vệ đường truyền: RSA - mã hóa username và password
- Bảo vệ dữ liệu trong database: hash password

2. Mã chứng thực văn bản (MAC - Message Authentication Code)
- Bảo vệ tính toàn vẹn của văn bản.
    - VD: Cho document <span>$M, c = h(M || k)$ (ghép $k$ là khóa bí mật của người chủ văn bản vào $M$</span>)

3. Chữ ký điện tử (Digital Signature)
Văn bản gốc <span>$M$, $C$ có $e, d$ (RSA), $A$ có khóa $k$</span> bí mật.

- Với <span>$A$: tạo mã chứng thực $a = \text{MAC}(M || k)$</span>.
- Với <span>$C$</span>: 
    - Nén M thành u: <span>$u = h(M)$</span>.
    - Chữ ký của người công chứng: <span>$s = \text{RSA}(d, u)$</span>
- Mọi người đều có thể kiểm tra: so sánh <span>$h(M) = \text{RSA}(e, s)$</span> 

### Phân tích hàm băm mật mã
Cho <span>$P$, tìm đụng độ $P'$</span>:
1. Tạo bảng <span>$t = 2^{\frac{n}{2}}$ biến thể của $P: P_1, P_2, ..$</span>
2. Lặp: <span>$\forall i \in t:$ chèn $(P_i, h(P_i))$ vào $t$</span>.
3. Tạo <span>$P'$, tra trong $t$</span>.

Kháng: cho <span>$n \geq 80k, (k > 1)$</span>

## 2. Chữ ký điện tử
**Nguyên lí chung**: dựa trên hệ mã public key cryptosystem <span>$f$</span>.
- <span>$s = f_d(m)$, chỉ có chủ giữ $d$</span> mới ký được
- Mọi người đều có <span>$e$, nên đều có thể kiểm tra $f^{-1}_e(s) = m$</span>

Tuy nhiên <span>$f$ ký rất chậm trên $m$. Thay vì vậy người ta ký trên hash $h(m)$, với $h$</span> là hàm băm mật mã.

### Naive version, using RSA:
Tạo key:
- Sử dụng pha tạo key của RSA tạo <span>$n, e, d$. Chú ý $e$ dùng để ký - bí mật, $d$</span> dùng để kiểm chứng - công khai.

Pha ký:
- Người ký tạo digest <span>$h$ từ document $m$, sau đó dùng RSA mã hóa $h$ thành chữ ký $s$ bằng khóa bí mật $e$</span>.
- Người ký công khai document <span>$m$, chữ ký $s$ và $n, d$</span>.

Pha kiểm chứng:    
- Người kiểm chứng tạo digest <span>$h$ từ document $m$</span>.
- Người kiểm chứng giải mã <span>$s$ thành $h'$, dùng $d, n$</span> với thuật toán RSA
- Nếu <span>$h' = h$, document $m$</span> được gửi đi toàn vẹn, không bị chỉnh sửa, đúng người ký.

[Cài đặt](https://github.com/trhgquan/CS155/tree/main/DSA).

### DSA (Digital Signature Algorithm) - DSS (Digital Signature Standard)
**Quan trọng**: Ký cần nhanh, verify không cần nhanh. Giải mã nhanh có cách (CRT).

1. Các tham số:
    - p là số nguyên tố (khoảng 512 bit).
    - q là số nguyên tố (khoảng 160 bit).
    - <span>$g \in \mathbb{Z}_N$ (bậc $g$ là bội của $q$</span>)
    - <span>$h: \{0, 1\}^{*} \rightarrow \{0, 1\}^{160}$</span>
    - <span>$x : 0 < x < q$</span> (khóa mật)
    - <span>$y \equiv g^x \pmod p$</span> (Diffie-Hellman - khóa công khai)
2. Ký văn bản <span>$m$</span>:
    - Chọn ngẫu nhiên <span>$k \in \mathbb{Z}_N$</span>
    - <span>$r \equiv (g^k \pmod p) \pmod q, s \equiv k^{-1}(h(m) + xr) \pmod q$ (Ký bằng khóa $x$</span>)
    - Kết quả là <span>$(r, s)$</span>.
3. Xác minh chữ ký:
    - <span>$t \equiv s^{-1} \pmod p$</span>
    - <span>$r \equiv (g^{h(m)t}y^{rt} \pmod p) \pmod q$ (Kiểm bằng khóa $y$</span>)



## 3. Zero-knowledge - tri thức trị không
<span>$A$ sử dụng khóa công khai $\pmod n$, $n = pq, p, q$ là số nguyên tố, $p, q \equiv 3 \pmod 4$</span>.

<span>$A$ thuyết phục người $B$</span> về khóa công khai là của mình:

1. <span>$A$</span> làm:
    - Chọn một <span>$s$ là số chính phương $\pmod n$, công bố $(n, s)$</span>
    - Tính <span>$t^2 \equiv s \pmod n$ và giữ bí mật $t$</span>.
2. <span>$A$</span> làm:
    - Chọn ngẫu nhiên <span>$r < n$</span>
    - <span>$z_1 \equiv r^2 \pmod n, z_2 \equiv sz_1^{-1} \pmod n$</span>
    - Gửi <span>$(z_1, z_2)$ cho $B$</span>.
3. <span>$B$</span> làm:
    - Kiểm <span>$s \equiv z_1z_2 \pmod n$</span>
    - Chọn 1 bit <span>$c \in \{0, 1\}$</span> 
    - Gửi <span>$c$ cho $A$</span>.
4. <span>$A$</span> làm:
    - <span>$c = 0$ thì gửi $r$</span>.
    - <span>$c = 1$ thì gửi $t^{r - 1}$</span>.
5. <span>$B$</span> làm:
    - <span>$c = 0$ thì kiểm $r^2 \equiv z_1 \pmod n$</span>.
    - <span>$c = 1$ thì kiểm $(t^{r - 1})^2 \equiv z_2 \pmod n$</span>.

Cách trên là Interactive Proving.

# 4. Hệ bảo mật thông tin

## Bảo mật CSDL
Không giống CSDL quan hệ thường học, CSDL có thể là file, record, row, col, ..

Xét CSDL <span>$D = \{f_1, f_2, .., f_n\}$ - plain. Ta muốn mã hóa $D$ thành $C$</span>

### Pha 1: Mã hóa CSDL
Sử dụng CRT để mã hóa CSDL.

1. Sinh <span>$n$ số nguyên tố $p_i$ khác nhau thỏa $p_i > f_i \forall i \in [1, n]$</span>
2. Giải hệ
    - <span>$X \equiv f_1 \pmod{p_1}$</span>
    - ...
    - <span>$X \equiv f_n \pmod{p_n}$</span>
3. <span>$C = X$ là mã hóa của $D$, $p_i$ là khóa để đọc $f_i$, gửi khóa $p_i$ này cho chủ của $f_i$</span>

### Pha 2: <span>$u_i$ đọc $f_i$</span>
4. <span>$f_i \equiv C \pmod{p_i}$</span>


## 5. Chia sẻ bí mật
### a. Đa thức nội suy Lagrange.
#### Định nghĩa
Đa thức <span>$P_n(x)$ bậc $n$ được sinh bởi $n$ cặp $(x_i, y_i)$</span>. Khi đó

<span>$\displaystyle P_n(x) = \sum_{j = 1}^{n} y_j L_j(x)$</span>

Với <span>$\displaystyle L_j(x) = \prod_{1 \leq m \leq n, m \neq j} \frac{x - x_m}{x_j - x_m}$</span>

#### Ví dụ: 
- với <span>$n = 2$, đa thức $\displaystyle P_2(x) = y_1\frac{x - x_2}{x_1 - x_2} + y_2\frac{x - x_1}{x_2 - x_1}$</span>
- với <span>$n = 3$, đa thức $\displaystyle P_3(x) = y_1\frac{(x - x_2)(x - x_3)}{(x_1 - x_2)(x_1 - x_3)} + y_2\frac{(x - x_1)(x - x_3)}{(x_2 - x_1)(x_2 - x_3)} + y_3\frac{(x - x_1)(x - x_2)}{(x_3 - x_1)(x_3 - x_2)}$</span>

### b. Ứng dụng: bài toán ngưỡng
Ví dụ: với ngưỡng <span>$n = 3$ và $N = 5$ người, hàm $P_3(x) = ax^2 + bx + c$. Khi đó $c$</span> là bí mật cần phải có 3 người cùng mở khóa mới có thể giải mã.

Ở đây ta chọn <span>$a = 5, b = 6, c = 4$, các phép toán thực hiện trong $\mathbb{Z}_7$. Hàm $P(x) = 5x^2 + 6x + 4$. Nên nhớ bước này hoàn toàn do người chọn, $a, b$ được giữ bí mật và $c$ là bí mật được chia sẻ. Ta cũng quy định mỗi người có cặp $(i, P(i))$ là khóa. Vậy 5 người lần lượt có các khóa $u_1 = (1, 1), u_2 = (2, 1), u_3 = (3, 4), u_4 = (4, 3), u_5 = (5, 5)$</span>.

Khi đó, nếu cần biết <span>$c$ thì cần 3 người dùng khóa của mình để mở. Khi đó ta tính $P(0)$ với các $x_1, x_2, x_3, y_1, y_2, y_3$</span> từ khóa của người dùng.

Ví dụ:
- Nếu <span>$u_1, u_2, u_3$ cùng nhau giải mã, khi đó $\displaystyle P(0) = 1\frac{(0 - 2)(0 - 3)}{(1 - 2)(1 - 3)} + 1\frac{(0 - 1)(0 - 3)}{(2 - 1)(2 - 3)} + 4\frac{(0 - 1)(0 - 2)}{(3 - 1)(3 - 2)} = 4$</span>
- Tương tự, chỉ cần 3 người cùng nhau giải mã sẽ thu được <span>$c$</span>.
