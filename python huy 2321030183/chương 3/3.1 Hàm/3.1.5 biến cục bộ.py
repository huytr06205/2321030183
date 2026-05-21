def msg():
    a = 10  # Biến cục bộ, chỉ tồn tại bên trong hàm msg
    print("giá trị của a là :", a)
    return

# Gọi hàm
msg()

# Nếu bạn chạy lệnh print(a) ở đây, Python sẽ báo lỗi NameError 
# vì biến a không tồn tại ở ngoài hàm.