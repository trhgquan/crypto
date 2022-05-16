# Hệ thống mã hóa đối xứng

- Còn gọi là mã hóa quy ước (conventional cryptosystem)
- Quy trình mã hóa và giải mã đều sử dụng chung một khóa
- Bảo mật thông tin phụ thuộc vào bảo mật khóa

## Các phương pháp truyền thống
- Phép thay thế (subtitution)
- Phép thay đổi vị trị (transposition)
    - Đơn ký tự (mono-alphabetic)
    - Đa ký tự (poly - alphabetic)

(xem lại CSC15005)



## Shift Cipher, mã hóa Caesar
Dịch chuyển xoay vòng từng ký tự đi $k$ vị trí. $k = 3$ là mã hóa Caesar.

Cho $\mathcal{P} = \mathcal{C} = \mathcal{K} = \mathbb{Z}_n$. Với mỗi khóa $k \in \mathcal{K}$, định nghĩa
- $e_k(x) = x + k \pmod n$ và $d_k(y) = y - k \pmod n; x, y \in \mathbb{Z}_n$
- $\mathcal{E} = \{e_k, k \in \mathcal{K}\}$ và $\mathcal{D} = \{d_k, k \in \mathcal{K}\}$

Tính chất:
- Phương pháp đơn giản
- Thao tác xử lý mã hóa & giải mã thực hiện nhanh
- Không gian khóa $\{0, 1, 2, .., n - 1\} = \mathbb{Z}_n$
- Dễ bị phá vỡ bằng brute-force.

## Subtitution Cipher
Hoán vị các phần tử trong bảng chữ cái. Tổng quát hơn: hoán vị (permute) các phần tử trong tập nguồn $\mathcal{P}$.

Cho $\mathcal{P} = \mathcal{C} = \mathbb{Z}_n, \mathcal{K}$ là tập hợp các hoán vị của $n$ phần tử $0, 1, .., n - 1$. Vậy, mỗi khóa $\pi \in \mathcal{K}$ là một hoán vị của $n$ phần tử $0, 1, .., n - 1$.

Với mỗi khóa $\pi \in \mathcal{K}$, định nghĩa:
- $e_{\pi}(x) = \pi(x)$ và $d_{\pi}(y) = \pi^{-1}(y); x, y \in \mathbb{Z}_n$
- $\mathcal{E} = \{e_{\pi}, \pi \in \mathcal{K}\}$ và $\mathcal{D} = \{d_{\pi}, \pi \in \mathcal{K}\}$

Tính chất:
- Đơn giản, thực hiện nhanh!
- Không gian khóa gồm $n!$ phần tử
- Brute-force với $k \in \mathcal{K}$ là không khả thi.
- Tấn công bằng cách khác: frequency analysis

(Ngoài lề): veni vidi vici - I came, I saw, I conquered

## Phương pháp Affine

Cho $\mathcal{P} = \mathcal{C} = \mathbb{Z}_n, \mathcal{K} = \{(a, b) \in \mathbb{Z}_n \times \mathbb{Z}_n: (a, n) = 1\}$. Với mỗi khóa $k = (a, b) \in \mathcal{K}$, định nghĩa:
- $e_k(x) = (ax + b) \pmod n$ và $d_k(y) = a^{-1}(y - b) \pmod n; x, y \in \mathbb{Z}_n$[^1]
- $\mathcal{E} = \{e_k, k \in \mathcal{K}\}$ và $\mathcal{D} = \{d_k, k \in \mathcal{K}\}$

Giải mã chính xác thì $e_k$ phải là song ánh, khi đó $(a, n) = 1$.

Gọi $\phi(n)$ (hàm phi Euler) là số lượng phần tử thuộc $\mathbb{Z}_n$ và nguyên tố cùng nhau với $n$.

Nếu $n = \prod_{i = 1}^{m} p_i^{e_i}$ với $p_i$ nguyên tố khác nhau đôi một, $e_i \in \mathbb{Z}^{+}, i \in [1, m]$ thì $\phi(n) = \prod_{i = 1}^{m}p_i^{e_i} - p_i^{e_i - 1}$ (number theory - xem lại).

Ta có
- $n$ khả năng chọn $b$
- $\phi(n)$ khả năng chọn $a$
- Vậy tổng cộng có $\phi(n) \times n$ giá trị $k = (a, b)$

## XEuclidean
Cho $a, b \in \mathbb{Z}$, xây dựng dãy sau:
- $r_0 = a$
- $r_1 = b$
- $s_0 = 1$
- $s_1 = 0$
- $t_0 = 0$
- $t_1 = 1$

Thực hiện:
- $r_2 = r_0 - q_0r_1$
- $s_2 = s_0 - q_0s_1$
- $t_2 = t_0 - q_0t_1$

Lặp đến khi $r_{k + 1} = 0$, khi đó $r_k = (a, b) = as_k + bt_k$

## Phương pháp Vigenere
Chọn $m \in \mathbb{Z}$. Định nghĩa $\mathcal{P} = \mathcal{C} = \mathcal{K} = (\mathbb{Z}_n)^m$
- $\mathcal{K} = \{(k_1, k_2, .., k_m)\} \in (\mathbb{Z}_n)^m$
- $\forall k = (k_1, k_2, .., k_m) \in \mathcal{K}, \forall x, y \in (\mathbb{Z}_n)^m$, định nghĩa
    - $e_k(x_1, x_2, .., x_m) = ((x_1 + k_1) \pmod n, (x_2 + k_2) \pmod n, .., (x_m + k_m) \pmod n)$
    - $d_k(y_1, y_2, .., y_m) = ((y_1 - k_1) \pmod n, (x_2 - k_2) \pmod n, .., (y_m - k_m) \pmod n)$

Mã hóa bằng thay thế: mỗi khóa $k$ được chọn, mỗi $x \in \mathcal{P}$ được ánh xạ duy nhất một $y \in \mathcal{C}$

Mã hóa Vigenere sử dụng khóa có độ dài $m$.
- Tên đặt theo Blaise de Vigenere
- Có thể xem như $m$ phép mã hóa bằng dịch chuyển luân phiên theo chu kỳ
- Không gian khóa $\mathcal{K}$ có số phần tử $n^m$
- VD: $m = 26, n = 5$ thì không gian khóa $\approx 1.1\times 10^7$

## Hill Cipher
(Xem lại CSC15005)

## Mã hóa bằng hoán vị
Trường hợp đặc biệt của mã hóa Hill.

Chọn số nguyên dương $m$. Định nghĩa
- $\mathcal{P} = \mathcal{C} = \mathbb{Z}_n^m$
- $\mathcal{K}$ là tập hoán vị của $m$ phần tử $\{1, 2, .., m\}$. Với mỗi $\pi \in \mathcal{K}$, định nghĩa
    - $e_{\pi}(x_1, x_2, .., x_m) = (x_{\pi(1)}, x_{\pi(2)}, .., x_{\pi(m)})$
    - $d_{\pi}(y_1, y_2, .., y_m) = (y_{\pi^{-1}(1)}, y_{\pi^{-1}(2)}, .., y_{\pi^{-1}(m)})$, với $\pi^{-1}$ là hoán vị ngược của $\pi$
