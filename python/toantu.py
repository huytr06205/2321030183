# Toán tử so sánh
a = 5
b = 10
a == b                          # False
a != b                          # True
a < b                           # True
a <= b                          # True
a > b                           # False
a >= b    

# Toán tử logic
x = True
y = False
x and y                         # False
x or y                          # True
not x                           # False

# Toán tử membership
"a" in "abc"                    # True
3 in [1, 2, 3]                  # True
"key" in {"key": "value"}       # True

# Toán tử identity
a = [1, 2, 3]
b = a
c = [1, 2, 3]
a is b                          # True (cùng object)
a is c                          # False (khác object)
a == c                          # True (cùng giá trị)

# Cộng
sum_result = a + b              # 13

# Trừ
sub_result = a - b              # 7

# Nhân
mul_result = a * b              # 30

# Chia (float division)
div_result = a / b              # 3.333...

# Chia lấy phần nguyên (integer division)
int_div_result = a // b         # 3

# Chia lấy dư (modulo)
mod_result = a % b              # 1

# Lũy thừa
power_result = a ** b           # 1000

# Ưu tiên toán tử
result = 2 + 3 * 4              # 14 (nhân trước)
result = (2 + 3) * 4            # 20 (cộng trước)


# --------- 8.2. TOÁN TỬ GÁN ---------
# Gán giá trị
x = 10

# Gán cộng
x += 5                          # x = x + 5 = 15

# Gán trừ
x -= 3                          # x = x - 3 = 12

# Gán nhân
x *= 2                          # x = x * 2 = 24

# Gán chia
x /= 4                          # x = x / 4 = 6.0

# Gán chia lấy phần nguyên
x //= 2                         # x = x // 2 = 3.0

# Gán chia lấy dư
x %= 2                          # x = x % 2 = 1.0

# Gán lũy thừa
x **= 3                         # x = x ** 3 = 1.0


# --------- 8.3. TOÁN TỬ SO SÁNH ---------
a = 5
b = 10

# Bằng
a == b                          # False

# Không bằng
a != b                          # True

# Nhỏ hơn
a < b                           # True

# Nhỏ hơn hoặc bằng
a <= b                          # True

# Lớn hơn
a > b                           # False

# Lớn hơn hoặc bằng
a >= b                          # False

# So sánh chuỗi
"abc" == "abc"                  # True
"abc" < "def"                   # True (so sánh theo thứ tự chữ cái)


# --------- 8.4. TOÁN TỬ LOGIC ---------
# AND logic
True and True                   # True
True and False                  # False
False and False                 # False

# OR logic
True or True                    # True
True or False                   # True
False or False                  # False

# NOT logic
not True                        # False
not False                       # True

# Kết hợp các toán tử logic
a = 10
b = 5
c = 15

(a > b) and (b < c)             # True and True = True
(a > b) or (b > c)              # True or False = True
not (a == b)                    # True

# Kỹ thuật short-circuit
x = 5
y = 10
# Nếu x < 0 sai, y không được kiểm tra
if (x < 0) and (y > 20):
    print("Both conditions are true")

# Nếu x > 0 đúng, y không được kiểm tra
if (x > 0) or (y < 5):
    print("At least one condition is true")
