a = []
s = 0 
n = int(input("Nhập số phần tử n: "))
for i in range(1, n + 1):
    k = int(input("Nhập phần tử thứ " + str(i) + ": "))
    a.append(k)
for i in a:
    s = s + i
print("Tổng của dãy là:" + str(s))

