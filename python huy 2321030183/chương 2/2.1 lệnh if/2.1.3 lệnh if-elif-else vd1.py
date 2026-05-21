# Nhập mã dân tộc từ bàn phím (kiểu số nguyên)
ma_dan_toc = int(input("Nhập vào mã dân tộc (1-5): "))

# Kiểm tra điều kiện bằng elif
if ma_dan_toc == 1:
    print("Dân tộc: Kinh")
elif ma_dan_toc == 2:
    print("Dân tộc: Tày")
elif ma_dan_toc == 3:
    print("Dân tộc: Nùng")
elif ma_dan_toc == 4:
    print("Dân tộc: Thái")
elif ma_dan_toc == 5:
    print("Dân tộc: Khơme")
else:
    print("Mã dân tộc không hợp lệ!")