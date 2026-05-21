# 1. Nhập ma trận 4x3 dưới dạng tuple lồng nhau từ bàn phím
# Hàm eval() giúp tự động chuyển chuỗi nhập vào thành cấu trúc Tuple trong Python
matrix = eval(input("Nhập ma trận 4x3 dưới dạng tuple: "))

# 2. In ra từng hàng theo định dạng danh sách [..] bằng cách ép kiểu sang list, không dùng vòng lặp for
print(list(matrix[0]))  # Kết quả hàng 1: [1, 2, 5]
print(list(matrix[1]))  # Kết quả hàng 2: [4, 5, 6]
print(list(matrix[2]))  # Kết quả hàng 3: [7, 8, 9]
print(list(matrix[3]))  # Kết quả hàng 4: [10, 11, 12]