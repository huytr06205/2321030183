# Tạo file foo.txt và ghi nội dung
fo = open("foo.txt", "w")
fo.write("python la mot ngon ngu lap trinh tuyet voi \n Minh cung nghi nhu the !\n")
fo.close()

# Mở lại file để kiểm tra các thuộc tính của tệp (sử dụng biến fo)
fo = open("foo.txt", "w")

print("Tên file là:", fo.name)
print("File đang mở ở chế độ:", fo.mode)
print("File đã đóng chưa?", fo.closed)

# Đóng file và kiểm tra lại thuộc tính đóng
fo.close()
print("Sau khi đóng, file đã đóng chưa?", fo.closed)