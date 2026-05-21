n = int(input("Nhập số lượng phần tử n (0 < n < 100): "))
while n <= 0 or n >= 100:
    n = int(input("Nhập lại n (0 < n < 100): "))

day_so = []
for i in range(n):
    x = float(input(f"Nhập phần tử thứ {i+1}: "))
    day_so.append(x)

# Lọc các số âm trong khoảng (-1000, -10)
mang_am = []
for so in day_so:
    if so < -10 and so > -1000:
        mang_am.append(so)  

if len(mang_am) > 0:
    tong = sum(mang_am)
    trung_binh = tong / len(mang_am)
    print(f"Trung bình cộng các số âm trong khoảng (-1000, -10): {trung_binh}")
else:
    print("Không có số âm nào trong khoảng (-1000, -10).")
 