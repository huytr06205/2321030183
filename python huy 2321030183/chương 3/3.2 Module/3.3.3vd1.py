a = []
n = int(input("nhập số phần tử của dãy số: "))

# Vòng lặp nhập các phần tử và thêm vào danh sách a
for i in range(1, n + 1):
    k = int(input("Nhập phần tử thứ " + str(i) + ": "))
    a.append(k)

# Mở file dulieu.txt tại ổ đĩa E (hoặc cùng thư mục nếu bạn không có ổ E)
obj = open("E:/dulieu.txt", "w")

# Duyệt qua danh sách và ghi từng số vào file, phân tách nhau bằng dấu cách
for i in a:
    obj.write(str(i) + " ")

# Đóng file
obj.close()