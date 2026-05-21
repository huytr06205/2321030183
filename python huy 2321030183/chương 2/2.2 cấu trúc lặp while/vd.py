# Nhập vào số phần tử trong tổng
n = int(input("Nhập n: "))

# Khởi tạo giá trị ban đầu cho biến tổng và biến đếm i
tong = 0
i = 1

# Vòng lặp chạy khi i vẫn nhỏ hơn hoặc bằng n
while i <= n:
    tong = tong + i  # Cộng dồn i vào tổng
    i = i + 1        # Tăng biến đếm i thêm 1 đơn vị

# In kết quả sau khi kết thúc vòng lặp
print("Tổng là", tong)