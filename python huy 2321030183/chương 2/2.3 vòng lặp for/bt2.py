n = int(input("nhập số ptử của dãy số: "))
a = []

# Nhập mảng tương tự bài 1
for i in range(1, n + 1):
    k = int(input("nhập phần tử thứ " + str(i) + ": "))
    a.append(k)

print("Lũy thừa 2 của các phần tử trong dãy:")
for i in a:
    # i ** 2 tương đương với i mũ 2 (lũy thừa 2)
    print(i ** 2)