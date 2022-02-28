# Tóm tắt kiến thức RSA

Các bước thực hiện:
1. Tính $n = p \times q$, với $p, q$ **nguyên tố** và **lớn**.

  Bước này áp dụng Định lý nhỏ Fermat để kiểm tra nhanh nguyên tố.

  Định lý nhỏ Fermat: $p \in P \Rightarrow \forall b: b^{p-1} \equiv 1 \pmod \phi$ (với $P$ là tập số nguyên tố)
  
  Để tạo một số nguyên tố **lớn**, tham khảo thuật toán tạo số nguyên tố lớn bên dưới.

2. Tính $\phi = (p - 1) \times (q - 1)$
3. Tính khóa giải $d$ và khóa mã $e$ sao cho $de \equiv 1 \pmod \phi$

  Từ công thức bên trên, $d \equiv e^{-1} \pmod \phi$.
  
  **Quan trọng**:
  - NÊN tạo khóa $d$ trước rồi tạo khóa $e$ theo $d$.
  - $\text{gcd}(d, \phi) = 1$ để tránh trường hợp message bị nhập nhằng sau khi mã hóa / giải mã. [Tham khảo](https://crypto.stackexchange.com/a/12256)
  
  Khi đó ta dùng [Extended Euclidean Algorithm](#Extended-Euclidean-Algorithm) để tìm nghịch đảo của $d$ trong modulo $\phi$.

4. Khóa giải $d$ giữ bí mật (private key), khóa $e$ công khai (public key):
  - $c \equiv m^e \pmod n$
  - $m^{*} \equiv c^d \pmod n$
  
  Quá trình này có sử dụng Định lý thặng dư Trung Hoa (cho nhanh).
  
Với các quá trình tính toán bên trên cần [thuật toán tính nhân + mũ modulo nhanh và hiệu quả](#Fast-multiply-and-exponential-modular).

Một số thuật toán bổ trợ:
- [Extended Euclidean Algorithm](#Extended-Euclidean-Algorithm) - tìm nhanh modulo nghịch đảo.
- [Fast multiply and Expotential Modular](#Fast-multiply-and-exponential-modular) - tính nhanh số mũ & nhân trong modulo.
- [Chinese Remainder Theorem](#Chinese-remainder-theorem) - định lý thặng dư Trung Hoa.
- [Large Prime Generator](#Large-prime-generator) - Tạo số nguyên tố lớn

# Extended Euclidean Algorithm

Thuật toán Euclide mở rộng - XEuclidean

Bổ đề Bézout: $\exists x, y \in \mathbb{Z}: ax + by = \text{gcd}(a, b)$. Trong trường hợp $a, b$ nguyên tố thì $ax + by = 1$.

Ở đây ta quan tâm đến trường hợp $a, b$ nguyên tố. Khi đó, $ax \equiv 1 \pmod b \Rightarrow x \equiv a^{-1} \pmod b$. Thuật toán XEuclidean sẽ trả về $\text{gcd}(a, b), x, y$ tương ứng với biểu diễn Bézout $ax + by = \text{gcd}(a, b)$.


```python
# Extended Euclidean Algorithm
def extended_gcd(a, b):
  if a == 0:
    return b, 0, 1

  g, y, x = extended_gcd(b % a, a)
  return g, x - (b // a) * y, y

# Example: Tìm và in biểu diễn Bézout với a = 7, b = 31;
a, b = 7, 31
g, x, y = extended_gcd(a, b)
print('{0}.{1} + {2}.{3} = {4}'.format(a, x, b, y, g))

# Finding inverse modulo with extended_gcd:
def inverse_modulo(a, m):
  g, x, y = extended_gcd(a, m)

  if g != 1:
    raise Exception('Inverse modular does not exists!')

  return x % m

# Example: Tìm nghịch đảo của 7 trong Z_{31}, 8 trong Z_{31}
print(inverse_modulo(7, 31))
print(inverse_modulo(8, 31))
```

    7.9 + 31.-2 = 1
    9
    4
    

# Fast multiply and exponential modular

Nhân naive có vẻ hơi "chậm". Vậy giờ ta xài bit manipulation!


```python
def add_mod(a, b, m):
  return (a + b) % m

# Các thuật toán tính nhanh modulo.

# (x * y) % m
def mul_mod(x, y, n):
  p = 0

  x %= n
    
  while y > 0:
    if y & 1:
      p = add_mod(p, x, n)
    
    x = (x << 1) % n

    y = y >> 1

  return p

# x^p % m
def pow_mod(x, p, n):
  y = 1

  x %= n
    
  if p == 0:
    return y

  while p > 0:
    if p & 1: 
      y = mul_mod(y, x, n)
    
    p = p >> 1
    
    x = mul_mod(x, x, n)
    
  return y

# Example:
# 3 * 50 = 14 (mod 17)
print(mul_mod(3, 50, 17))

# 3 ^ 50 = 9 (mod 17)
print(pow_mod(3, 50, 17))
```

    14
    9
    

# Chinese Remainder Theorem

Định lý thặng dư Trung Hoa (Tầu-khựa) - CRT

Cho hệ phương trình đồng dư
$$\begin{cases}
x \equiv b_1 \pmod{m_1} \\ 
x \equiv b_2 \pmod{m_2} \\
.. \\
x \equiv b_n \pmod{m_n}
\end{cases}
$$

yêu cầu đặt ra là tìm $x$?

## Phương pháp giải
1. Tính $N = m_1 \times m_2 \times .. \times m_n$
2. Tính $\displaystyle N_1 = \frac{N}{m_1}, N_2 = \frac{N}{m_2}, .., N_n = \frac{N}{m_n}$
3. Tính $x_1 \equiv N_1^{-1} \pmod{m_1}, x_2 \equiv N_2^{-1} \pmod{m_2}, .., x_n \equiv N_n^{-1} \pmod{m_n}$

  Tìm modulo nghịch đảo của $N_i$ trong modulo $m_i$, $i \in [1, n]$). Gợi ý: xài thuật Extended Euclidean bên trên.
  
4. Đáp án của bài toán: $\displaystyle x \equiv \sum_{i = 1}^{n} (x_i \times N_i \times b_i) \pmod N$

  Hay, $\displaystyle x = Nk + \sum_{i = 1}^{n} (x_i \times N_i \times b_i), k \in \mathbb{N}$
  
## Áp dụng trong RSA
Ta có thể sử dụng CRT để giải mã nhanh RSA cipher. Xét $c^d \pmod{n} \equiv c^d \pmod{pq}$. 

Đặt $d_1 \equiv d \pmod{p - 1}, d_2 \equiv d \pmod{q - 1}$. $\exists n_1, n_2: d = n_1(p - 1) + d_1 = n_2(q - 1) + d_2$.

Áp vào công thức ban đầu, ta có $c^d \pmod{pq} \equiv c^{d_1}c^{(p - 1)} \pmod{p}$. Mà theo định lý nhỏ Fermat, $c^{p - 1} \equiv 1 \pmod{p}$. Vậy $c^{d} \equiv c^{d_1} \pmod{p}$

Tương tự, $c^{d} \equiv c^{d_2} \pmod{q}$. Vậy ta có hệ phương trình đồng dư

$$\begin{cases}
c^{d} \equiv c^{d_1} \pmod{p} \\
c^{d} \equiv c^{d_2} \pmod{q} 
\end{cases}
$$

Ưu điểm của phương pháp này là thực hiện ít phép mũ hơn so với việc phải tính $c^d$.

Code (naive) và ví dụ bên dưới lần lượt giải các hệ

$$
1.
\begin{cases}
x \equiv 1 \pmod{2} \\
x \equiv 2 \pmod{3} 
\end{cases}
\\
2.
\begin{cases}
x \equiv 2 \pmod{3} \\
x \equiv 0 \pmod{2} \\
x \equiv 0 \pmod{5} 
\end{cases}
\\
3.
\begin{cases}
x \equiv 2 \pmod{3} \\
x \equiv 1 \pmod{7} 
\end{cases}
$$


```python
# Naive solution to the Chinese Remainder Theorem
def chinese_remainder(b, m):
  # Calculate N
  N = 1
  for i in m: N *= i
    
  # Calculate N_i
  Ni = [N // i for i in m]

  # Calculate x^{-1}_i
  reverse_x = [inverse_modulo(n, m[i]) for i, n in enumerate(Ni)]

  result = 0

  for i, x in enumerate(reverse_x):
    result = add_mod(mul_mod(Ni[i], mul_mod(b[i], x, N), N), result, N)
    
  return N, result
        
print('{0[0]}k + {0[1]}'.format(chinese_remainder([1, 2], [2, 3])))
print('{0[0]}k + {0[1]}'.format(chinese_remainder([2, 0, 0], [3, 2, 5])))
print('{0[0]}k + {0[1]}'.format(chinese_remainder([2, 1], [3, 7])))
```

    6k + 5
    30k + 20
    21k + 8
    

# Large prime generator

## 1. Định lý: 
Cho $p$ là một số nguyên tố lẻ, $k \in \mathbb{N+}$ thỏa $1 < k < 2(p+1), k \nmid p$. Đặt $n = 2kp + 1$, các phát biểu sau là tương đương:

1. $n$ là số nguyên tố
2. $\exists a: 2 < a < N$ sao cho

$$
\begin{cases}
a^{kp} \equiv -1 \pmod{n} \\
\text{gcd}(a^k + 1, n) = 1
\end{cases}
$$

## 2. Thuật toán
1. Chọn số **nguyên tố** $p_1$ có $d_1$ chữ số.
2. Tìm $k_1 < 2(p_1 + 1)$ sao cho $p_2 = 2k_1p_1 + 1$ có $d_2$ chữ số và $\exists a_1 < p_2$ thỏa
$$
\begin{cases}
a^{k_1p_1} \equiv -1 \pmod{p_2} \\
\text{gcd}(a_1^{k_1} + 1, p_2) = 1
\end{cases}
$$

Khi đó $p_2$ là một số nguyên tố. Tiếp tục thay $p_1 \leftarrow p_2$ và thực hiện lại từ bước 2 đến khi đạt được số nguyên tố có số chữ số $d_1$ cần tạo. 

**Quan trọng**: Đây là phương pháp brute-force để tìm một số nguyên tố lớn. Vì vậy, nên generate trước 1 cặp nguyên tố lớn trước khi xài trong RSA.


```python
def large_prime_generator(expected_length, seed, collision = 1):
  p1 = seed
  d1 = len(str(p1))

  while (d1 <= expected_length):
    found = 0
    for k1 in range(2, 2 * (p1 + 1) + 1):
      p2 = 2 * k1 * p1 + 1
      d2 = len(str(p2))

      if d2 > expected_length: break
      if p2 % 10 == 5: continue

      # print('Testing {0} (k = {1})'.format(p2, k1))
      for a1 in range(2, p2 + 1, collision):
        power_mod = pow_mod(a1, k1 * p1, p2)
        egcd = extended_gcd(a1**k1 + 1, p2)[0]

        if power_mod == p2 - 1 and egcd == 1:
          # print(p2, ' valid')
          found = 1
          break

      if found == 1: break

    if found == 1:
      p1 = p2
      d1 = len(str(p1))

    if d2 >= expected_length: break

  return p1

# Generate a prime with 5 digits, but with different seed
print(large_prime_generator(5, 13))
print(large_prime_generator(5, 17))
```

    19319
    34679
    
