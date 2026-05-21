# ========== 9. VÒNG LẶP (FOR) ==========
# For loop với list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# For loop với range
for i in range(5):              # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):           # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):       # 0, 2, 4, 6, 8 (bước nhảy 2)
    print(i)

# For loop với enumerate
for index, fruit in enumerate(fruits):
    print(index, fruit)

# For loop với zip
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(name, age)

# For loop với dictionary
person = {"name": "Alice", "age": 25}
for key, value in person.items():
    print(key, value)

# Nested loop
for i in range(3):
    for j in range(3):
        print(i, j)

# List comprehension
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]           # [1, 4, 9, 16, 25]
evens = [x for x in numbers if x % 2 == 0] # [2, 4]

# Dictionary comprehension
squares_dict = {x: x**2 for x in numbers}   # {1: 1, 2: 4, ...}

# Set comprehension
squares_set = {x**2 for x in numbers}       # {1, 4, 9, 16, 25}


# ========== 10. VÒNG LẶP (WHILE) ==========
count = 0
while count < 5:
    print(count)
    count += 1

# Break và Continue
for i in range(10):
    if i == 3:
        continue                # Bỏ qua i=3
    if i == 7:
        break                   # Dừng vòng lặp
    print(i)

# While với break
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == "quit":
        break
    print(f"You entered: {user_input}")

# Else trong loop
for i in range(5):
    if i == 10:
        break
else:
    print("Loop completed normally")