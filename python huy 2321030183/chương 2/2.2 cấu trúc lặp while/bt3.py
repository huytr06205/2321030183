n = int(input("nhập số n: "))
i = 2

print("Các ước số ngtố của n:")

while i <= n:
    # Kiểm tra xem i có phải là ước của n không
    if n % i == 0:
        j = 2
        nguyen_to = True
        
        # Vòng lặp kiểm tra xem i có phải số nguyên tố không
        while j < i:
            if i % j == 0:
                nguyen_to = False
                break
            j = j + 1
            
        # Nếu i là số nguyên tố thì in ra
        if nguyen_to:
            print(i)
            
    i = i + 1