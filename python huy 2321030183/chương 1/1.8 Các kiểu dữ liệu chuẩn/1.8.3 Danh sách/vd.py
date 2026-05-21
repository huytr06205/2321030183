# Giả sử chuỗi S được nhập vào từ bàn phím hoặc khai báo trực tiếp
S = "2 4 6 7 9"

# Bước 1: Dùng phương thức split() để tách chuỗi thành danh sách các ký tự số
chuoi_tach = S.split()  # Kết quả: ['2', '4', '6', '7', '9']

# Bước 2: Dùng hàm int() để ép kiểu từng phần tử thành số nguyên (dùng list comprehension)
ma_tran_1_chieu = [int(x) for x in chuoi_tach]

# Bước 3: In kết quả ra màn hình
print("Ma trận 1 chiều của chuỗi số là:", ma_tran_1_chieu)
# Kết quả in ra: [2, 4, 6, 7, 9]