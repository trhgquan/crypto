# Hệ thống mã hóa

Là bộ năm $ (\mathbb{P}, \mathbb{C}, \mathbb{K}, \mathbb{E}, \mathbb{D}) $ thỏa mãn các điều kiện sau:

- Tập nguồn $ \mathbb{P} $ là tập hữu hạn các mẩu tin nguồn cần mã hóa có thể có
- Tập đích $ \mathbb{C} $ là tập hữu hạn các mẩu tin có thể có sau khi mã hóa
- Tập khóa $ \mathbb{K} $ là tập hữu hạn các khóa có thể được sử dụng
- Tập $ \mathbb{E} $ và $ \mathbb{D} $ là tập luật mã hóa và giải mã. $ \forall k \in \mathbb{K}: \exists e_k \in \mathbb{E}, \exists d_k \in \mathbb{D}$ sao cho:
    - Luật mã hóa: $e_k: \mathbb{P} \rightarrow \mathbb{C}$
    - Luật giải mã: $d_k: \mathbb{C} \rightarrow \mathbb{P}$
  
  2 luật này thỏa mãn $d_k(e_k(x)) = x, \forall x \in \mathbb{P}$

- **Bảo đảm mẩu tin $x$ được mã hóa bằng luật $e_k$ có thể được giải mã bằng luật $d_k$**

## So sánh hệ mã đối xứng và bất đối xứng

|Nội dung|Mã hóa đối xứng|Mã hóa bất đối xứng|
|--------|---------------|-------------------|
|Tốc độ|Nhanh|Chậm|
|Chiều dài khóa|Ngắn|Dài|
|Trao đổi mã khóa|Khó|Dễ|
|Tên gọi khóa|Secret key|Public-private key|

## Tính chất của $\mathbb{Z}_m$
### Phép cộng trong $\mathbb{Z}_m$
- $\forall a, b \in \mathbb{Z}_m: a + b \in \mathbb{Z}_m$
- Giao hoán: $\forall a, b \in \mathbb{Z}_m: a + b = b + a$
- Kết hợp: $\forall a, b, c \in \mathbb{Z}_m: (a + b) + c = a + (b + c)$
- Phần tử trung hòa là $0$, $\forall a \in \mathbb{Z}_m: a + 0 = 0 + a = a$
- Phần tử đối: $\forall a, b \in \mathbb{Z}_m$ đều có phần tử đối là $(m - a) \in \mathbb{Z}_m$

### Phép nhân trong $\mathbb{Z}_m$
- $\forall a, b \in \mathbb{Z}_m: a \times b \in \mathbb{Z}_m$
- Giao hoán: $\forall a, b \in \mathbb{Z}_m: a \times b = b \times a$
- Kết hợp: $\forall a, b, c \in \mathbb{Z}_m: (a \times b) \times c = a \times (b \times c)$
- Phần tử đơn vị là $1$, $\forall a \in \mathbb{Z}_m: a \times 1 = 1 \times a = a$
- Phân phối phép $\times$ với phép $+$: $\forall a, b, c \in \mathbb{Z}_m, (a + b) \times c = a\times c + b\times c$
