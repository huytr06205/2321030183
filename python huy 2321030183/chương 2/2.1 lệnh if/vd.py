# Nhập dữ liệu từ bàn phím và chuyển sang kiểu số thực (float)
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
c = float(input("Nhập số thứ ba: "))

# Thuật toán tìm số lớn nhất
max_val = a  # Giả định ban đầu a là số lớn nhất

if b > max_val:
    max_val = b  # Cập nhật max nếu b lớn hơn

if c > max_val:
    max_val = c  # Cập nhật max nếu c lớn hơn

# In kết quả ra màn hình bằng cách định dạng chuỗi kiểu cũ (%)
print("Số lớn nhất trong ba số %f, %f và %f là %f" % (a, b, c, max_val))