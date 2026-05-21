# Câu 4: Tính tổng a + b và tìm chữ số lớn nhất trong tổng đó

a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))

tong = a + b
tam = tong
chu_so_lon_nhat = 0

while tam > 0:
    chu_so = tam % 10

    if chu_so > chu_so_lon_nhat:
        chu_so_lon_nhat = chu_so

    tam //= 10

print("Tổng a + b là:", tong)
print("Chữ số lớn nhất trong tổng là:", chu_so_lon_nhat)