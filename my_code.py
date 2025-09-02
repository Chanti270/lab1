# my_code.py

# Print numbers from 0 to 9
for i in range(10):
    print(f"Number {i}")

# Function to greet names
def greet(name):
    print(f"Hello, {name}!")

names = ["Alice", "Bob", "Charlie", "David", "Eve"]
for n in names:
    greet(n)

# More functions to reach 30+ lines
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

for i in range(5):
    print(f"{i} squared is {multiply(i, i)}")

# End of file
