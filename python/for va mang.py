

def read_int(prompt=''):
	while True:
		try:
			return int(input(prompt))
		except ValueError:
			print('Vui lòng nhập một số nguyên hợp lệ.')

def main():
	n = read_int('Nhập số phần tử n: ')
	if n <= 0:
		print('Không có phần tử để tính tổng.')
		return

	print('Nhập', n, 'số nguyên (mỗi số nhấn Enter):')
	total = 0
	i = 0
	while i < n:
		x = read_int()
		total += x
		i += 1

	print('Tổng của dãy là:', total)

if __name__ == '__main__':
	main()

