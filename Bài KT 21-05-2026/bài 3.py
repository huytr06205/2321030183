n = int(input("Nhap n: "))

tich = 1
for chu_so in str(abs(n)):
    tich *= int(chu_so)

print("Tich cac chu so =", tich)

if tich % 2 == 0 and tich > 20:
    print("Tich la so chan va lon hon 20")
else:
    print("Tich khong thoa man dieu kien") 