n = int(input("n = "))
s = 0

# Vòng lặp tìm ước số thực sự của n từ 1 đến n-1
for i in range(1, n):
    if n % i == 0:
        s = s + i  # Cộng dồn ước số vào tổng s

# Kiểm tra nếu tổng các ước bằng chính số đó
if s == n:
    print(n, "là số hoàn hảo")
else:
    print(n, "không phải là số hoàn hảo")