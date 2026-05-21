# Chương trình tách số và chữ từ file input.txt ra 2 file outso.txt và outchu.txt
try:
    with open("input.txt", "r", encoding="utf-8") as tep:
        noi_dung = tep.read()
except FileNotFoundError:
    print("Không tìm thấy file input.txt!")
    exit()
so = ""
chu = ""
for ky_tu in noi_dung:
    if ky_tu.isdigit():
        so += ky_tu
    elif ky_tu.isalpha():
        chu += ky_tu
with open("outso.txt", "w", encoding="utf-8") as tep_so:
    tep_so.write(so)
with open("outchu.txt", "w", encoding="utf-8") as tep_chu:
    tep_chu.write(chu)
print("Đã tách xong dữ liệu!")
