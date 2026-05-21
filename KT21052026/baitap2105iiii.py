# Câu 5: Kiểm tra m có chia hết cho tổng các chữ số của n hay không

m = int(input("Nhập số nguyên dương m: "))
n = int(input("Nhập số nguyên dương n: "))

tong_chu_so_n = 0
tam = n

while tam > 0:
    chu_so = tam % 10
    tong_chu_so_n += chu_so
    tam //= 10

print("Tổng các chữ số của n là:", tong_chu_so_n)

if m % tong_chu_so_n == 0:
    print(m, "chia hết cho tổng các chữ số của", n)
else:
    print(m, "không chia hết cho tổng các chữ số của", n)