# Nhập 2 số nguyên dương
a = int(input("Nhap a: "))
b = int(input("Nhap b: "))

# Tìm chữ số nhỏ nhất của b
chu_so_nho_nhat = min(str(b))
chu_so_nho_nhat = int(chu_so_nho_nhat)

print("Chu so nho nhat cua b =", chu_so_nho_nhat)

# Kiểm tra chia hết
if chu_so_nho_nhat != 0 and a % chu_so_nho_nhat == 0:
    print("a chia het cho chu so nho nhat cua b")
else:
    print("a khong chia het cho chu so nho nhat cua b")