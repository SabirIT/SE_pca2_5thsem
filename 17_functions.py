# Functions in Python

# Basic function
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# Default parameter
def greet_with_title(name, title="Mr."):
    return f"Hello, {title} {name}!"

print(greet_with_title("Smith"))
print(greet_with_title("Johnson", "Dr."))

# Multiple return values
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 4, 1, 5, 9, 2])
print(f"Min: {low}, Max: {high}")

# *args - variable number of arguments
def add_all(*args):
    return sum(args)

print(f"Sum: {add_all(1, 2, 3, 4, 5)}")

# **kwargs - keyword arguments
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print("Student Info:")
display_info(name="Bob", age=20, grade="A")

# Nested function
def outer():
    message = "Hello from outer"
    def inner():
        print(message)
    inner()

outer()

# Function as argument (higher-order function)
def apply(func, value):
    return func(value)

def double(x):
    return x * 2

print(f"Double of 7: {apply(double, 7)}")

# Docstring
def factorial(n):
    """Return the factorial of a non-negative integer n."""
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(f"Factorial of 5: {factorial(5)}")
print(f"Docstring: {factorial.__doc__}")
