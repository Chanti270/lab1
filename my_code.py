# my_code.py - Lab 1 CS202
# Author: Chanti
# Demonstrates functions, loops, and lists

def greet(name):
    """Greet the user by name."""
    print(f"Hello, {name}!")

def sum_numbers(numbers):
    """Return the sum of a list of numbers."""
    total = 0
    for num in numbers:
        total += num
    return total

def factorial(n):
    """Return factorial of n."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def fibonacci(n):
    """Return first n Fibonacci numbers as a list."""
    fib_seq = [0, 1]
    while len(fib_seq) < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq[:n]

def main():
    """Main function for Lab 1."""
    greet("Chanti")

    numbers = [1, 2, 3, 4, 5]
    print("Numbers:", numbers)
    print("Sum:", sum_numbers(numbers))

    n = 5
    print(f"Factorial of {n}:", factorial(n))

    fib_count = 10
    print(f"First {fib_count} Fibonacci numbers:", fibonacci(fib_count))

    print("Even numbers up to 10:")
    for i in range(2, 11, 2):
        print(i, end=" ")
    print()

    squares = [x ** 2 for x in range(1, 6)]
    print("Squares of 1 to 5:", squares)

if __name__ == "__main__":
    main()
