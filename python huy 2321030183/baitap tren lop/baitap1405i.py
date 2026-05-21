# Nhập vào 2 số nguyên dương m và n
m = int(input("Nhập số nguyên dương m: "))
n = int(input("Nhập số nguyên dương n: "))

tong = m + n
tam = tong
chu_so_lon_nhat = 0

# Tìm chữ số lớn nhất trong tổng
while tam > 0:
    chu_so = tam % 10

    if chu_so > chu_so_lon_nhat:
        chu_so_lon_nhat = chu_so

    tam = tam // 10

print("Tổng m + n là:", tong)
print("Chữ số lớn nhất trong tổng là:", chu_so_lon_nhat)