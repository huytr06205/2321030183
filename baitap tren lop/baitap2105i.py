
# Câu 2: Kiểm tra tổng các chữ số của n có chia hết cho 3 không

n = int(input("Nhập số nguyên dương n: "))

tong_chu_so = 0
tam = n

while tam > 0:
    chu_so = tam % 10
    tong_chu_so += chu_so
    tam //= 10

print("Tổng các chữ số của", n, "là:", tong_chu_so)

if tong_chu_so % 3 == 0:
    print("Tổng các chữ số chia hết cho 3")
else:
    print("Tổng các chữ số không chia hết cho 3")