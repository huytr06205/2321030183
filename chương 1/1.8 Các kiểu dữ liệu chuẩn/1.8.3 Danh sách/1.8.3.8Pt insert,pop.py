list1 = ['java', 'python', 'sql']

# insert(index, obj): Chèn 'c++' vào vị trí chỉ mục 1
list1.insert(1, 'c++') 
print(list1)  # Kết quả: ['java', 'c++', 'python', 'sql']

# pop([index]): Xóa và trả về phần tử tại vị trí index. Nếu không ghi index, xóa phần tử cuối cùng
list1.pop()   
print(list1)  # Kết quả: ['java', 'c++', 'python']