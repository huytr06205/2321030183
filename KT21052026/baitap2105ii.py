# Câu 3: Kiểm tra tích các chữ số của n có phải số chẵn và lớn hơn 20 không

n = int(input("Nhập số nguyên dương n: "))

tich_chu_so = 1
tam = n

while tam > 0:
    chu_so = tam % 10
    tich_chu_so *= chu_so
    tam //= 10

print("Tích các chữ số của", n, "là:", tich_chu_so)

if tich_chu_so % 2 == 0 and tich_chu_so > 20:
    print("Tích các chữ số là số chẵn và lớn hơn 20")
else:
    print("Tích các chữ số không thỏa mãn điều kiện")