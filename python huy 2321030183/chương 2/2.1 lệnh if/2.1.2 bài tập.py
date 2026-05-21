# Nhập vào 2 số thực x, y từ bàn phím
x = float(input("Nhập x: "))
y = float(input("Nhập y: "))

# Kiểm tra từng trường hợp riêng biệt
if x > y:
    print(x, "lớn hơn", y)

if x < y:
    print(x, "nhỏ hơn", y)

if x == y:
    print(x, "bằng", y)