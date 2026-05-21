# Nhập điểm 3 môn từ bàn phím
a = float(input("nhập điểm toán : "))
b = float(input("nhập điểm lý : "))
c = float(input("nhập điểm hóa : "))

# Tính điểm trung bình
tb = (a + b + c) / 3
print("Điểm tb :", tb)

# Biện luận xếp loại bằng cấu trúc if - elif - else
if tb < 5:
    print("yếu")
elif tb < 7:
    print("TB")
elif tb < 9:
    print("khá")
else:
    print("giỏi")