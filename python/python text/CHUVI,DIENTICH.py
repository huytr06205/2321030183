chieu_dai = float(input("\nNhập chiều dài (cm): "))
chieu_rong = float(input("Nhập chiều rộng (cm): "))

# Kiểm tra dữ liệu hợp lệ
if chieu_dai <= 0 or chieu_rong <= 0:
    print("\nLỗi: Chiều dài và chiều rộng phải lớn hơn 0!")
else:
    # Tính chu vi
    chu_vi = 2 * (chieu_dai + chieu_rong)

    # Tính diện tích
    dien_tich = chieu_dai * chieu_rong

    # Hiển thị kết quả
    print(f"Chu vi: {chu_vi} cm")
    print(f"Diện tích: {dien_tich} cm²")
    