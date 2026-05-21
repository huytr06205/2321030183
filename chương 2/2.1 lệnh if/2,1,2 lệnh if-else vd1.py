# Nhập vào một số nguyên từ bàn phím
n = int(input("Nhập 1 số nguyên: "))

# Kiểm tra điều kiện chia hết cho 2
if n % 2 == 0:
    # Hàm repr(n) dùng để chuyển số n thành chuỗi văn bản
    print("Số " + repr(n) + " là số chẵn")
else:
    print("Số " + repr(n) + " là số lẻ")