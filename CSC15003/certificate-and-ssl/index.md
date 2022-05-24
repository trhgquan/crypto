# Certificate và SSL

## Digital Certificate & Digital Authority
- Digital Certificate: chứng thư số, chứng nhận thực sự sở hữu khóa công khai.
    - Thông tin người sở hữu
    - Khóa công khai
    - Chữ ký của bên thứ ba đáng tin cậy
- Chuẩn digital cert: X509.
- Digital Authority: đơn vị thứ ba đáng tin cậy, quản lý chữ ký điện tử và chứng thư số.

## Secured Socket Layer (SSL)

- Có nhiều phiên bản SSL: 1.0, 2.0, 3.0
- TLS: phát triển dựa trên SSL 3.0, có các phiên bản 1.0, 1.1, 1.2, 1.3

### TLS protocol
- Handshake: dùng asymmetric crypto tạo khóa bí mật dùng chung (shared secret key) giữa client và server.
- Record: dùng khóa bí mật trong giao thức handshake để bảo vệ quá trình giao tiếp giữa client và server.
