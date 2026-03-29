# List Comprehensions in Python

# Basic list comprehension
squares = [x**2 for x in range(1, 11)]
print(f"Squares: {squares}")

# With condition (filter)
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# Nested list comprehension
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(f"Matrix: {matrix}")

# Flatten a nested list
nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flat = [item for sublist in nested for item in sublist]
print(f"Flattened: {flat}")

# String processing with comprehension
words = ["hello", "world", "python", "rocks"]
capitalized = [word.capitalize() for word in words]
print(f"Capitalized: {capitalized}")

lengths = [len(word) for word in words]
print(f"Lengths: {lengths}")

# Conditional expression in comprehension
numbers = [-3, -1, 0, 2, 4, -5, 7]
abs_values = [x if x >= 0 else -x for x in numbers]
print(f"Absolute values: {abs_values}")

# Set comprehension
unique_lengths = {len(word) for word in words}
print(f"Unique word lengths: {unique_lengths}")

# Dictionary comprehension
word_lengths = {word: len(word) for word in words}
print(f"Word-length dict: {word_lengths}")

# Generator expression (memory efficient)
gen = (x**2 for x in range(1, 6))
print(f"Generator values: {list(gen)}")
