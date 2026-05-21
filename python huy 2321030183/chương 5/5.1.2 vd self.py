# Định nghĩa lớp Hình tròn
class circle:
    # Phương thức tính diện tích
    def Dientich(self):
        # Công thức: bán kính * bán kính * 3.141592
        return self.bk * self.bk * 3.141592
        
    # Phương thức nhập bán kính từ bàn phím
    def Nhap(self):
        self.bk = float(input("Nhập bKính: "))

# Khởi tạo đối tượng và chạy chương trình
c = circle()
c.Nhap()
print("Dtích của htròn la: ", c.Dientich())