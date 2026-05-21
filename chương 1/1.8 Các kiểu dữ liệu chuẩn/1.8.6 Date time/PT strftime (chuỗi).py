import datetime

# Lấy thời gian hiện tại của hệ thống
now = datetime.datetime.now()
print("Thời gian hiện tại chưa định dạng:", now)

# Định dạng thành chuỗi dạng: ngày/tháng/năm giờ:phút:giây
s = now.strftime("%d/%m/%Y %H:%M:%S")
print("S :", s)
# Kết quả ví dụ: S : 08/08/2021 04:44:32 (tùy thuộc vào thời gian chạy máy)