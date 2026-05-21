# Nhập số lượng số thực n (0 < n < 100)
n = int(input("Nhập số phần tử n: "))
while n <= 0 or n >= 100:
    n = int(input("Nhập lại n (0 < n < 100): "))

tong = 0
dem = 0

# Vòng lặp nhập các số thực x và kiểm tra điều kiện
for i in range(n):
    x = float(input(f"Nhập số thực x_{i+1}: "))
    # Kiểm tra nếu x là số âm và nằm trong khoảng (-1000, -10)
    if -1000 < x < -10:
        tong += x
        dem += 1

# Tính và in kết quả trung bình cộng (TBC)
if dem > 0:
    tbc = tong / dem
    print("Trung bình cộng các số thỏa mãn là:", tbc)
else:
    print("Không có số nào thỏa mãn điều kiện.")