# Ví dụ về toán tử membership (in, not in)
a = 10
b = 2
list_data = [1, 2, 3, 4, 5]  # Lưu ý: Đổi tên biến 'list' thành 'list_data' để tránh trùng từ khóa hệ thống

print(a in list_data)        # Kết quả: False (vì 10 không có trong danh sách)
print(b in list_data)        # Kết quả: True  (vì 2 có trong danh sách)
print(a not in list_data)    # Kết quả: True  (đúng là 10 không nằm trong danh sách)
print(b not in list_data)    # Kết quả: False (sai vì 2 có nằm trong danh sách)