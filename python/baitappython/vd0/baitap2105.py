
# Câu 1: Tính trung bình cộng các phần tử dương nằm trong khoảng (0, 1000)

so_luong = int(input("Nhập số lượng phần tử n (0 < n < 100): "))

tong_duong = 0
dem_duong = 0

for i in range(so_luong):
    gia_tri = float(input(f"Nhập x[{i + 1}]: "))

    if 0 < gia_tri < 1000:
        tong_duong += gia_tri
        dem_duong += 1

if dem_duong > 0:
    trung_binh = tong_duong / dem_duong
    print("Trung bình cộng các phần tử dương trong khoảng (0, 1000) là:", trung_binh)
else:
    print("Không có phần tử dương nào nằm trong khoảng (0, 1000)")