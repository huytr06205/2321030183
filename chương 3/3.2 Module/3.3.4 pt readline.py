# Mở file toanco.txt ở chế độ đọc
f = open("E:/toanco.txt", "r")

# Đọc dòng đầu tiên
l1 = f.readline()
print("Dòng 1:", l1)

# Đọc dòng thứ hai (con trỏ tự động chuyển sang dòng tiếp theo)
l2 = f.readline()
print("Dòng 2:", l2)

f.close()