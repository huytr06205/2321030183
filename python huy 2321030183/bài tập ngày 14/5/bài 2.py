# Nhập số phần tử
n = int(input("Nhap n: "))

tong = 0

# Nhập dãy số nguyên
for i in range(n):
    x = int(input(f"Nhap x{i+1}: "))
    
    # Kiểm tra số chẵn
    if x % 2 == 0:
        tong += x

print("Tong cac phan tu chan =", tong)

# Kiểm tra điều kiện
if tong % 7 == 0 and tong < 200:
    print("Tong chia het cho 7 va nho hon 200")
else:
    print("Tong khong thoa man dieu kien")