# Nhập hai hệ số a và b từ bàn phím (kiểu số nguyên)
a = int(input("a: "))
b = int(input("b: "))

# Biện luận nghiệm của phương trình
if a == 0:
    if b == 0:
        print("Phương trình vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
else:
    x = -b / a
    print("x =", x)