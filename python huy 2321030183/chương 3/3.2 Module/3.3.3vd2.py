m = int(input("nhập số hàng = "))
n = int(input("nhập số cột = "))
a = []

# 1. Vòng lặp lồng nhau để nhập dữ liệu ma trận từ bàn phím
for i in range(0, m):
    a.append([])  # Tạo một hàng trống mới
    for j in range(0, n):
        k = int(input("Nhập phần tử a[%d][%d]: " % (i + 1, j + 1)))
        a[i].append(k)

# 2. Mở file matran.txt ở chế độ ghi
obj = open("matran.txt", "w")

# 3. Ghi dữ liệu ma trận vào file theo đúng cấu trúc dòng và cột
for i in range(0, m):
    for j in range(0, n):
        # Ghi phần tử và thêm dấu cách phía sau
        obj.write(str(a[i][j]) + " ")
    obj.write("\n")  # Ghi ký tự xuống dòng sau khi kết thúc một hàng

# 4. Đóng file
obj.close()
print("Đã lưu ma trận thành công vào file matran.txt!")