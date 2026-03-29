# Lambda Functions in Python

# Basic lambda
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

# Lambda with multiple arguments
add = lambda a, b: a + b
print(f"3 + 7 = {add(3, 7)}")

# Lambda with conditional expression
absolute = lambda x: x if x >= 0 else -x
print(f"Absolute of -10: {absolute(-10)}")

# Using lambda with sorted()
students = [("Alice", 85), ("Bob", 72), ("Carol", 91), ("Dave", 68)]
sorted_by_score = sorted(students, key=lambda s: s[1])
print(f"Sorted by score: {sorted_by_score}")

sorted_by_name = sorted(students, key=lambda s: s[0])
print(f"Sorted by name: {sorted_by_name}")

# Using lambda with map()
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(f"Squares: {squares}")

# Using lambda with filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")

# Using lambda with reduce()
from functools import reduce
product = reduce(lambda a, b: a * b, numbers)
print(f"Product of {numbers}: {product}")

# Immediately Invoked Lambda
result = (lambda x, y: x * y)(6, 7)
print(f"6 * 7 = {result}")
