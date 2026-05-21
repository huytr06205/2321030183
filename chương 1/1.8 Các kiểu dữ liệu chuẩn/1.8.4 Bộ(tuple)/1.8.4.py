# Cú pháp khởi tạo đầy đủ: ( <giá trị thứ nhất>, <giá trị thứ hai>, ..., <giá trị thứ n> )

tup = (1, 2, 3, 4)
print(tup)        # Kết quả: (1, 2, 3, 4)

e_tup = ()        # Khởi tạo tuple rỗng
print(e_tup)      # Kết quả: ()

# Phương thức count: Trả về số lần xuất hiện của một giá trị trong Tuple
# Cú pháp: <Tuple>.count(value)
tup_demo = (1, 2, 3, 2, 4)
print(tup_demo.count(2))  # Kết quả ví dụ: 2