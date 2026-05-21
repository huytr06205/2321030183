# ============================================
# NHỮNG BÀI CODE CƠ BẢN PYTHON
# ============================================

# 1. IN RA MÀN HÌNH (PRINT)
print("Xin chào Python!")
print("1 + 2 =", 1 + 2)
    
# 2. BIẾN VÀ KIỂU DỮ LIỆU
name = "An"           # Chuỗi (String)
age = 20              # Số nguyên (Integer)
height = 1.75         # Số thực (Float)
is_student = True     # Boolean

print(name, age, height, is_student)

# 3. NHẬP DỮ LIỆU TỪ BÀN PHÍM
# name = input("Nhập tên của bạn: ")
# print("Xin chào", name)

# 4. CÁC PHÉP TOÁN CƠ BẢN
a = 10
b = 3

print("Cộng:", a + b)           # 13
print("Trừ:", a - b)            # 7
print("Nhân:", a * b)           # 30
print("Chia:", a / b)           # 3.333...
print("Chia lấy phần nguyên:", a // b)  # 3
print("Chia lấy dư:", a % b)    # 1
print("Lũy thừa:", a ** b)      # 1000

# 5. CÂU LẠC ĐIỀU KIỆN (IF-ELSE)
score = 85

if score >= 90:
    print("Điểm A")
elif score >= 80:
    print("Điểm B")
elif score >= 70:
    print("Điểm C")
else:
    print("Điểm dưới C")

# 6. VÒNG LẶP FOR
print("\nVòng lặp For:")
for i in range(5):
    print(f"Lần lặp {i}")

# In bảng cửu chương 3
print("\nBảng cửu chương 3:")
for i in range(1, 10):
    print(f"3 x {i} = {3 * i}")

# 7. VÒNG LẶP WHILE
print("\nVòng lặp While:")
count = 1
while count <= 5:
    print(f"Số đếm: {count}")
    count += 1

# 8. DANH SÁCH (LIST)
fruits = ["Táo", "Chuối", "Cam", "Dâu"]
print("\nDanh sách trái cây:", fruits)
print("Trái cây đầu tiên:", fruits[0])
print("Trái cây cuối cùng:", fruits[-1])

# Thêm phần tử
fruits.append("Nho")
print("Sau khi thêm:", fruits)

# Duyệt danh sách
for fruit in fruits:
    print(f"- {fruit}")

# 9. TỪ ĐIỂN (DICTIONARY)  
student = {
    "name": "Lan",
    "age": 20,
    "grade": "K20"
}

print("\nThông tin học sinh:", student)
print("Tên:", student["name"])
print("Tuổi:", student["age"])

# 10. HÀM (FUNCTION)
def greet(name):
    return f"Xin chào {name}!"

print("\n" + greet("Minh"))

def calculate_sum(a, b):
    """Hàm tính tổng hai số"""
    return a + b

result = calculate_sum(5, 7)
print(f"Tổng 5 + 7 = {result}")

# 11. CHUỖI (STRING)
text = "Python là ngôn ngữ lập trình"
print("\nChuỗi:", text)
print("Độ dài chuỗi:", len(text))
print("In hoa:", text.upper())
print("In thường:", text.lower())
print("Chia cắt:", text.split())

# 12. XỬ LÝ NGOẠI LỆ (TRY-EXCEPT)
try:
    number = int(input("Nhập một số: "))
    result = 10 / number
    print(f"10 / {number} = {result}")
except ValueError:
    print("Lỗi: Bạn phải nhập một số!")
except ZeroDivisionError:
    print("Lỗi: Không thể chia cho 0!")

# 13. DANH SÁCH COMPREHENSION
numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers]
print("\nBình phương:", squared)

# 14. LAMBDA FUNCTION
add = lambda x, y: x + y
print("Lambda (1 + 2):", add(1, 2))

# 15. IMPORT MODULE
import math
print("\nPi =", math.pi)
print("Căn bậc 2 của 16 =", math.sqrt(16))
