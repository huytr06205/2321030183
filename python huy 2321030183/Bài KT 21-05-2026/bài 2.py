n = int(input("Nhap n: "))

tong = 0
for chu_so in str(abs(n)):
    tong += int(chu_so)

print("Tong cac chu so =", tong)

if tong % 3 == 0:
    print("Tong chia het cho 3")
else:
    print("Tong khong chia het cho 3") 