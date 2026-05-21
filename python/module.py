# ========== MODULE PYTHON CƠ BẢN ==========

import os
import sys
import random
import math
import json
from datetime import datetime, timedelta
from collections import Counter, defaultdict

# OS - Làm việc với hệ điều hành
os.getcwd()                     # Thư mục hiện tại
os.listdir(".")                 # Liệt kê file
os.path.exists("file.txt")      # Kiểm tra tồn tại
os.path.join("d:", "folder")    # Join đường dẫn

# SYS - Hệ thống
sys.argv                        # Đối số dòng lệnh
sys.version                     # Phiên bản Python
sys.platform                    # Platform (win32, linux, ...)
sys.exit()                      # Thoát chương trình

# RANDOM - Số ngẫu nhiên
random.random()                 # 0.0 - 1.0
random.randint(1, 10)           # 1 - 10
random.choice([1, 2, 3])        # Chọn ngẫu nhiên
random.shuffle(list)            # Trộn list

# MATH - Toán học
math.sqrt(16)                   # 4.0
math.ceil(4.3)                  # 5
math.floor(4.9)                 # 4
math.factorial(5)               # 120
math.gcd(12, 8)                 # 4
math.pi                         # 3.14159...
math.e                          # 2.71828...

# JSON
json.dumps(dict)                # Dict -> JSON string
json.loads(json_string)         # JSON string -> Dict
json.dump(data, file)           # Ghi vào file
json.load(file)                 # Đọc từ file

# DATETIME
datetime.now()                  # Thời gian hiện tại
datetime(2025, 12, 25)          # Tạo datetime
datetime.strptime("2025-12-25", "%Y-%m-%d")  # Parse
timedelta(days=7)               # Khoảng thời gian

# COLLECTIONS
Counter([1, 1, 2, 2, 2, 3])    # Counter({'2': 3, '1': 2, '3': 1})
defaultdict(list)               # Dict với default value

# STRING
import string
string.digits                   # "0123456789"
string.ascii_letters            # "abcdefghijk...XYZ"
string.punctuation              # "!\"#$%..."

# ITERTOOLS
from itertools import combinations, permutations
combinations([1, 2, 3], 2)      # [(1,2), (1,3), (2,3)]
permutations([1, 2])            # [(1,2), (2,1)]

# COPY
import copy
copy.copy(list)                 # Shallow copy
copy.deepcopy(list)             # Deep copy

# TIME
import time
time.time()                     # Timestamp hiện tại
time.sleep(2)                   # Dừng 2 giây
time.ctime()                    # Dạng readable
