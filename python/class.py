# ========== 13. LỚP VÀ ĐỐI TƯỢNG (CLASS) ==========
# Định nghĩa lớp
class Car:
    # Biến lớp (shared giữa tất cả instances)
    total_cars = 0

    # Constructor
    def __init__(self, brand, model, year):
        self.brand = brand          # Biến instance
        self.model = model
        self.year = year
        Car.total_cars += 1

    # Method
    def drive(self):
        return f"{self.brand} {self.model} is driving"

    # Method với tham số
    def accelerate(self, speed):
        return f"Accelerating at {speed} km/h"

    # String representation
    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"

    # Class method
    @classmethod
    def from_string(cls, car_string):
        brand, model, year = car_string.split(",")
        return cls(brand, model, int(year))

    # Static method
    @staticmethod
    def is_vintage(year):
        return 2025 - year > 20

# Tạo đối tượng
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2022)

# Truy cập thuộc tính
print(car1.brand)               # "Toyota"
print(car1.year)                # 2020

# Gọi method
print(car1.drive())             # "Toyota Camry is driving"
print(car1.accelerate(100))     # "Accelerating at 100 km/h"
print(str(car1))                # "2020 Toyota Camry"

# Class method
car3 = Car.from_string("Ford,Mustang,2018")

# Static method
print(Car.is_vintage(2000))     # True

# Kiểm tra biến lớp
print(Car.total_cars)           # 3