class circle:
    pi = 3.141592
    
    # Hàm khởi tạo __init__ với giá trị mặc định radius = 1
    def __init__(self, radius=1):
        self.bk = radius
        
    # Phương thức tính diện tích
    def Dientich(self):
        return self.bk * self.bk * circle.pi

# Khởi tạo đối tượng với radius = 5
c = circle(5)
print("Dtích htron la: ", c.Dientich())