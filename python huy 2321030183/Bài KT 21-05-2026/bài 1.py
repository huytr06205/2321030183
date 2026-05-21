n = int(input("Nhap n (0 < n < 100): "))
while n <= 0 or n >= 100:
    print("Gia tri n phai nam trong khoang 0 < n < 100")
    n = int(input("Nhap lai n: "))

tong = 0.0
dem = 0

for i in range(n):
    x = float(input(f"Nhap x{i+1}: "))
    if 0 < x < 1000:
        tong += x
        dem += 1

if dem > 0:
    tbc = tong / dem
    print("Trung binh cong cac phan tu duong trong khoang (0, 1000) =", tbc)
else:
    print("Khong co phan tu duong thoa man")