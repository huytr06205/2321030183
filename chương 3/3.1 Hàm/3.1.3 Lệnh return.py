# Định nghĩa hàm tính giai thừa của một số m bất kỳ
def giai_thua(m):
    gt = 1
    # Vòng lặp nhân dồn từ 1 đến m
    for i in range(1, m + 1):
        gt = gt * i
    return gt  # Trả về kết quả giai thừa tính được

# --- Chương trình chính ---
# Nhập số nguyên n từ bàn phím
n = int(input("nhập n: "))

# Gọi hàm giai_thua và truyền biến n vào làm đối số
ket_qua_gt = giai_thua(n)

print("Giai thừa của", n, "là:", ket_qua_gt)