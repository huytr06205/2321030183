n = int(input("Nhập số lượng phần tử n (0 < n < 200): "))
while n <= 0 or n >= 200:
    n = int(input("Nhập lại n (0 < n < 200): "))

day_so = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    day_so.append(x)
 
tong_chan = 0
for so in day_so:
    if so % 2 == 0:
        tong_chan += so

print(f"Tổng các số chẵn trong dãy là: {tong_chan}")

if tong_chan % 7 == 0 and tong_chan < 200:
    print("Tổng các số chẵn chia hết cho 7 và nhỏ hơn 200.")
else:
    print("Tổng các số chẵn không thỏa mãn điều kiện.")
