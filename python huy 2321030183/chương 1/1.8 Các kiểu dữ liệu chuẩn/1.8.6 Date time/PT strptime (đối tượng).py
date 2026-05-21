from datetime import datetime

# Chuỗi ngày tháng ban đầu
dt_string = "11/07/2021"

# Chuyển đổi chuỗi trên thành đối tượng datetime dựa vào định dạng tương ứng (%d/%m/%Y)
ngay_thang = datetime.strptime(dt_string, "%d/%m/%Y")
print(ngay_thang)
# Kết quả: 2021-07-11 00:00:00