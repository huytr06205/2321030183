# Nhập hai hệ số a và b từ bàn phím (kiểu số thực)
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))

# Biện luận các trường hợp xảy ra
if a == 0 and b == 0:
    print("Phương trình vô số nghiệm")
elif a == 0 and b != 0:
    print("Phương trình vô nghiệm")
else:
    x = -b / a
    print("Phương trình có 1 nghiệm duy nhất x =", x)