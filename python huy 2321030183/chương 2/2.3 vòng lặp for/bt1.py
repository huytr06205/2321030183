a = []
s = 0
n = int(input("nhập số ptử của dãy số: "))

# Vòng lặp nhập các phần tử và thêm vào mảng a
for i in range(1, n + 1):
    k = int(input("nhập phần tử thứ " + str(i) + ": "))
    a.append(k)

# Vòng lặp duyệt qua từng phần tử trong mảng a để tính tổng
for i in a:
    s = s + i

print("Tổng của dãy số là: " + str(s))