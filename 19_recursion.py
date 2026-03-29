# Recursion in Python

# Factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(f"Factorial of 6: {factorial(6)}")

# Fibonacci using recursion
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

fib_series = [fibonacci(i) for i in range(10)]
print(f"First 10 Fibonacci: {fib_series}")

# Sum of digits using recursion
def sum_of_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)

print(f"Sum of digits of 12345: {sum_of_digits(12345)}")

# Power using recursion
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

print(f"2^10 = {power(2, 10)}")

# GCD using recursion (Euclidean algorithm)
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(f"GCD of 48 and 18: {gcd(48, 18)}")

# Reverse a string using recursion
def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]

print(f"Reverse of 'Python': {reverse_string('Python')}")

# Tower of Hanoi
def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"  Move disk 1 from {source} to {target}")
        return
    hanoi(n - 1, source, auxiliary, target)
    print(f"  Move disk {n} from {source} to {target}")
    hanoi(n - 1, auxiliary, target, source)

print("Tower of Hanoi (3 disks):")
hanoi(3, "A", "C", "B")
