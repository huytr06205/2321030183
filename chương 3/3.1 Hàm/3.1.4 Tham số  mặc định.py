# Định nghĩa hàm sum với tham số b có giá trị mặc định là 10
def sum(a, b=10):
    return a + b

# Trường hợp 1: Truyền đầy đủ cả 2 đối số (a=1, b=2). Giá trị mặc định b=10 bị ghi đè.
print(sum(1, 2))  
# Kết quả: 3

# Trường hợp 2: Chỉ truyền 1 đối số (a=5). Tham số b tự động lấy giá trị mặc định là 10.
print(sum(5))     
# Kết quả: 15