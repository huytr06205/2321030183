# Khởi tạo lại dictionary
dic = {'name': 'abc', 'member': 69}

# Thay đổi giá trị của khóa 'name' thành 'deg'
dic['name'] = 'deg'
print(dic)
# Kết quả: {'name': 'deg', 'member': 69}

# Tăng giá trị của khóa 'member' lên 1 đơn vị
dic['member'] = dic['member'] + 1
print(dic)
# Kết quả: {'name': 'deg', 'member': 70}