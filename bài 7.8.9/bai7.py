def la_so_nguyen_to(a):
    if a < 2:
        return False
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False
    return True

n = int(input("Nhập n: "))
day = [int(input(f"Nhập phần tử thứ {i+1}: ")) for i in range(n)]

tong = sum(so for so in day if la_so_nguyen_to(so))
print("Tổng các số nguyên tố là:", tong)

if tong % 2 != 0 and tong > 50:
    print("Tổng là số lẻ và lớn hơn 50")
else:
    print("Tổng không thỏa điều kiện")