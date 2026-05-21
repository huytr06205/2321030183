n = int(input("Nhập số tự nhiên n: "))

if n <= 1:
    print("Không có ước số nguyên tố cho n =", n)
else:
    n_ban_dau = n
    uoc_nguyen_to = []
    i = 2

    while i * i <= n:
        if n % i == 0:
            uoc_nguyen_to.append(i)

            while n % i == 0:
                n = n // i
        else:
            i = i + 1

    if n > 1:
        uoc_nguyen_to.append(n)
  
    if len(uoc_nguyen_to) == 0:
        print("Không có ước số nguyên tố cho n =", n_ban_dau)
    else:
        print("Ước số nguyên tố của", n_ban_dau, "là:", end=" ")
        j = 0
        while j < len(uoc_nguyen_to):
            print(uoc_nguyen_to[j], end=" ")
            j = j + 1