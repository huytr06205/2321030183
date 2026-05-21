a = int(input("Nhap a (so nguyen duong): "))
while a <= 0:
    print("a phai la so nguyen duong")
    a = int(input("Nhap lai a: "))

b = int(input("Nhap b (so nguyen duong): "))
while b <= 0:
    print("b phai la so nguyen duong")
    b = int(input("Nhap lai b: "))

Tong = a + b
print("Tong =", Tong)

chu_so_lon_nhat = int(max(str(Tong)))
print("Chu so lon nhat =", chu_so_lon_nhat)