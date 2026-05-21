nums = [int(input(f"Nhập số thứ {i+1}: ")) for i in range(3)]
tong = sum(nums)
print("Tổng là:", tong)
so_chan = sum(1 for x in str(tong) if int(x) % 2 == 0)
print("Số chữ số chẵn trong tổng là:", so_chan)
