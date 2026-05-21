# Mở file matran.txt ở chế độ đọc
f = open("E:/matran.txt", "r")

# Đọc từng dòng, cắt các khoảng trắng và tách thành danh sách các số
# (Sửa lỗi cú pháp viết tắt List Comprehension trong vở)
ma = [dong.split() for dong in f]

print("Ma trận đọc được từ file:", ma)

s = 0
# Vòng lặp lồng nhau duyệt qua từng hàng (subma) và từng phần tử (j) trong ma trận
for subma in ma:
    for j in subma:
        s = s + float(j)

print("Tổng của ma trận là:", s)

f.close()