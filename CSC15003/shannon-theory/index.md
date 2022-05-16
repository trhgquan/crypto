# Lý thuyết Shannon

Hay là lý thuyết về độ an toàn thông tin

## Lý thuyết Bayes

Gọi $P(X = x)$ là xác suất biến ngẫu nhiên $X$ nhận giá trị $x$, $P(Y = y)$ là xác suất biến ngẫu nhiên $Y$ nhận giá trị $y$.

Xác suất có điều kiện <span>$P(x | y)$</span> là xác suất $X = x$ khi đã biết $Y = y$.

Xác suất $P(x, y)$ là xác suất $X = x$ và $Y = y$.

Ta có:
- $X$ và $Y$ là hai biến ngẫu nhiên độc lập khi $P(x, y) = P(x)P(y)$
- Định lý Bayes: <span>$\displaystyle P(x | y) = \frac{P(y | x)P(x)}{P(y)}$</span>. Chú ý ta sẽ gọi $P(x)$ là a priori (tiên nghiệm) và <span>$P(x | y)$</span> là a posteriori (hậu nghiệm). Cũng từ đây có thể suy ra rằng $X$ và $Y$ độc lập nếu <span>$P(x | y) = P(x)$</span>.

## An toàn tuyệt đối (Perfect Security)
$\forall x \in \mathcal{P}$ là tập plaintext, $\forall k \in \mathcal{K}$ là tập khóa. Gọi 
- <span>$P_{\mathcal{P}}(x | c)$</span> là xác suất plaintext là $x$ khi ciphertext là $c$
- $P_{\mathcal{P}}(x)$ là xác suất plaintext là $x$
- <span>$P_{\mathcal{K}}(k | c)$</span> là xác suất khóa mã là $k$ khi ciphertext là $c$
- $P_{\mathcal{K}}(k)$ là xác suất khóa mã là $k$


Một hệ mã đạt chuẩn an toàn tuyệt đối khi đối với plaintext và khóa, xác suất hậu nghiệm bằng xác suất tiên nghiệm. Hay,
$\forall x \in \mathcal{P}, \forall k \in \mathcal{K}$:
- <span>$P_{\mathcal{P}}(x | c) = P_{\mathcal{P}}(x)$</span>
- <span>$P_{\mathcal{K}}(k | c) = P_{\mathcal{K}}(k)$</span>

Phát biểu ngắn: hệ mã đạt an toàn tuyệt đối khi <span>$|\mathcal{K}| = |\mathcal{P}|$</span>

Ý nghĩa: Kẻ tấn công không khai thác được gì từ ciphertext. 

## Định lý Shannon

Cho hệ $(\mathcal{P}, \mathcal{K}, \mathcal{C}, \mathcal{E}, \mathcal{D})$,
- $\forall c \in \mathcal{C}, \exists k \in \mathcal{K}: e_k(x) = c$
- <span>$\displaystyle \forall k \in \mathcal{K}, P_{\mathcal{K}}(k) = \frac{1}{|\mathcal{K}|}$</span>

## Vernam Cipher
Khóa là dãy giá trị random đủ dài, thuật toán mã hóa như sau:
- $C = P \oplus K$
- $M = C \oplus K$

Ưu điểm:
- Thuật toán mã hóa dễ
- Perfect Security

Nhược điểm:
- Khóa không tái sử dụng
- Kích thước khóa lớn (e.g mã hóa file 10GB thì kích thước khóa cũng là 10GB)

## Entropy
Biểu diễn lượng thông tin mà một biến ngẫu nhiên có thể cung cấp; có thể hiểu đơn giản là độ dài bit cần thiêt để biểu diễn.

$\displaystyle \text{entropy}(X) = \sum_{x \in \mathcal{X}} P(X = x)\log_2(P(X = x))$
