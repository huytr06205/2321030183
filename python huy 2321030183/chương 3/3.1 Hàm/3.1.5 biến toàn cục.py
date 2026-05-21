b = 20  # Biến toàn cục, có thể truy cập ở bất kỳ đâu

def msg():
    a = 10  # Biến cục bộ
    print("Giá trị của a là", a)
    print("giá trị của b là", b)  # Hàm đọc được giá trị của biến toàn cục b
    return

# Gọi hàm
msg()

# In biến toàn cục ở ngoài hàm
print(b)