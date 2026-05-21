# Nhập số hàng m và số cột n
m = int(input("Nhap m = "))
n = int(input("Nhap n = "))
a = []

# Vòng lặp nhập ma trận
for i in range(0, m):
    a.append([])  # Thêm một hàng trống vào ma trận
    for j in range(0, n):
        # Nhập phần tử cho hàng i, cột j (chỉ số hiển thị từ 1 để người dùng dễ nhìn)
        k = float(input("Nhap ptu thu a[%d][%d]: " % (i + 1, j + 1)))
        a[i].append(k)

print("Mang vua nhap la : ")
# Vòng lặp in ma trận ra màn hình
for i in range(0, m):
    for j in range(0, n):
        # In mỗi phần tử chiếm khoảng rộng 8 ký tự, có 2 chữ số thập phân
        print("%8.2f" % a[i][j], end=" ")
    print()  # Xuống dòng khi in xong một hàng