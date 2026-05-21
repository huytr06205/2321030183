m = int(input("Nhap m (so nguyen duong): "))
while m <= 0:
    print("m phai la so nguyen duong")
    m = int(input("Nhap lai m: "))

n = int(input("Nhap n (so nguyen duong): "))
while n <= 0:
    print("n phai la so nguyen duong")
    n = int(input("Nhap lai n: "))

sum_digits = 0
for digit in str(n):
    sum_digits += int(digit)

print(f"Tong cac chu so cua n = {sum_digits}")

if m % sum_digits == 0:
    print(f"{m} chia het cho {sum_digits}")
else:
    print(f"{m} khong chia het cho {sum_digits}")