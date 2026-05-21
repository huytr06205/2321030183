
def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Vui lòng nhập số nguyên hợp lệ.")


def main():
    print("Nhập số hàng (m) và số cột (n):")
    m = read_int("m = ")
    n = read_int("n = ")

    if m <= 0 or n <= 0:
        print("Số hàng và số cột phải là số nguyên dương.")
        return

    matrix = []

    for i in range(m):
        while True:
            try:
                row = list(map(int, input(f"Hàng {i+1}: ").split()))
                if len(row) != n:
                    print(f"Cần {n} phần tử. Nhập lại.")
                    continue
                matrix.append(row)
                break
            except ValueError:            
                print("Chỉ được nhập số nguyên.")

    print("Ma trận vừa nhập:")
    for row in matrix:
        print(*row)

   
if __name__ == "__main__":
    main()