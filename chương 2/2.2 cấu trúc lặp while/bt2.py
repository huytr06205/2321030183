tong = 0

while True:
    n = int(input("nhập số : "))
    
    # Nếu nhập số 0 thì thoát vòng lặp
    if n == 0:
        break
        
    # Nếu là số chẵn thì cộng dồn vào tổng
    if n % 2 == 0:
        tong = tong + n

print("Tổng các số chẵn là:", tong)