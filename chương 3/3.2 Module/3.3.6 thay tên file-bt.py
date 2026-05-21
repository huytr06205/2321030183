# Mở file đầu vào để đọc và file đầu ra để ghi dữ liệu
fi = open("input.txt", "r")
fo = open("output.txt", "w")

# Duyệt qua từng dòng trong file input.txt
for line in fi:
    line = line.strip()
    if line == "":  # Bỏ qua nếu là dòng trống
        continue
        
    n = int(line)
    k = 2
    
    # Thực hiện thuật toán phân tích thừa số nguyên tố của số n
    while n > 1:
        # Nếu k là ước của n
        if n % k == 0:
            # Ghi thừa số nguyên tố k vào file output.txt
            fo.write(str(k) + " ")
            
            # Chia bỏ toàn bộ các ước k trùng lặp
            while n % k == 0:
                n = n // k
        else:
            k = k + 1  # Tăng k nếu không phải là ước
            
    # Xuống dòng trong file output sau khi phân tích xong một số
    fo.write("\n")

# Đóng cả hai file sau khi xử lý xong
fi.close()
fo.close()
print("Đã phân tích và lưu kết quả vào tệp output.txt!")