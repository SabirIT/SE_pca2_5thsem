# Variables and Data Types in Python

# Integer
age = 25
print(f"Integer: {age}, Type: {type(age)}")

# Float
pi = 3.14159
print(f"Float: {pi}, Type: {type(pi)}")

# String
name = "Python"
print(f"String: {name}, Type: {type(name)}")

# Boolean
is_active = True
print(f"Boolean: {is_active}, Type: {type(is_active)}")

# NoneType
value = None
print(f"None: {value}, Type: {type(value)}")

# Complex
z = 3 + 4j
print(f"Complex: {z}, Type: {type(z)}")

# Type conversion
num_str = "42"
num_int = int(num_str)
num_float = float(num_str)
print(f"String '{num_str}' converted to int: {num_int}, float: {num_float}")

# Multiple assignment
x = y = w = 10
print(f"x={x}, y={y}, w={w}")

# Swap variables
a, b = 5, 10
a, b = b, a
print(f"After swap: a={a}, b={b}")
