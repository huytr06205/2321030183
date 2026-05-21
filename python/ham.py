# ========== 11. HÀM (FUNCTION) ==========
# Hàm cơ bản
def greet():
    print("Hello!")

greet()

# Hàm có tham số
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")

# Hàm có giá trị mặc định
def greet_with_title(name, title="Mr"):
    print(f"Hello, {title} {name}!")

greet_with_title("Alice")
greet_with_title("Alice", "Ms")

# Hàm có return
def add(a, b):
    return a + b

result = add(5, 3)              # 8

# Hàm trả về nhiều giá trị
def get_min_max(numbers):
    return min(numbers), max(numbers)

min_val, max_val = get_min_max([1, 5, 3, 9, 2])

# Hàm với *args (số lượng tham số không xác định)
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

sum_all(1, 2, 3, 4, 5)

# Hàm với **kwargs (từ khóa tham số)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="Hanoi")

# Hàm với *args và **kwargs
def my_function(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

my_function(1, 2, 3, name="Alice", age=25)

# Lambda function (hàm ẩn danh)
square = lambda x: x**2
square(5)                       # 25

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))

# Decorator (cơ bản)
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def my_function():
    print("Function is running")

my_function()