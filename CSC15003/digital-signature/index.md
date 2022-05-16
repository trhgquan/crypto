# Digital Signature

## Mục tiêu
- Authentication
- Data Integrity
- Non-repudiation

Digital signature = Digital Signature generation algorithm + digital signature verification algorithm

## Chữ ký đính kèm (appendix)
- Đi kèm với thông điệp gốc
- Sử dụng hash function thay cho redundency function.

1. $m_h \rightarrow h(m)$
2. Ký: $s \rightarrow S(m_h, k)$
3. Kiểm tra: $V(s, k) = m_h$

## Khôi phục thông điệp
1. $m_r = R(m)$
2. Ký: $s = S(m_r, k)$
3. Kiểm tra: $m_r = V(s, k)$
4. Khôi phục: $m = R^{-1}(m_r)$

## Tấn công
Cách tấn công:
- Key-only: chỉ biết public key
- Message attack
    - Known-message: xài nhiều chữ ký
    - Chosen-message: chọn lọc chữ ký
    - Adaptive-chosen: dùng người ký như oracle (chương trình), generate chữ ký từ input có sẵn sau đó thử generate chữ ký mà không cần oracle.

Mức độ phá (nghiêm trọng dần):
- Existential forgery: tạo ra chữ ký hợp lệ dựa trên tài liệu dễ nhận biết.
- Selective forgery: tạo ra chữ ký hợp lệ dựa trên thông điệp (lộ thuật).
- Total break: tìm được cách phá (lộ private key).

## Tấn công RSA
- Phân tích thừa số nguyên tố
- Nhiều cặp khóa cho cùng chữ ký
