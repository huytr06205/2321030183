# Mở file ở chế độ đọc ("r")
f = open("E:/dulieu.txt", "r")

# Đọc toàn bộ nội dung file thành một chuỗi văn bản
s = f.read()

# Loại bỏ các khoảng trắng thừa ở đầu và cuối chuỗi (sửa lỗi chữ sthip trong vở)
s = s.strip()

# Cắt chuỗi thành danh sách các ký tự số dựa vào dấu cách " "
a = s.split(" ")
t = 0

print("Dãy số đọc được là: ", a)

# Duyệt qua từng ký tự số, chuyển sang kiểu số nguyên rồi cộng dồn vào t
for i in a:
    if i != "":  # Kiểm tra tránh phần tử rỗng nếu file có dấu cách thừa
        t = t + int(i)

print("Tổng của dãy số là: ", t)

# Đóng file sau khi dùng xong
f.close()