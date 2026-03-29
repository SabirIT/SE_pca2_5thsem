# Tuple Operations in Python

# Create a tuple
coordinates = (10.5, 20.3, 5.0)
print(f"Tuple: {coordinates}")

# Access elements
print(f"X: {coordinates[0]}, Y: {coordinates[1]}, Z: {coordinates[2]}")

# Slicing
t = (1, 2, 3, 4, 5)
print(f"Slice [1:4]: {t[1:4]}")

# Tuple is immutable - cannot change elements
# coordinates[0] = 99  # This would raise a TypeError

# Length
print(f"Length: {len(coordinates)}")

# Count and Index
nums = (1, 2, 2, 3, 2, 4)
print(f"Count of 2: {nums.count(2)}, Index of 3: {nums.index(3)}")

# Check membership
print(f"3 in t: {3 in t}")

# Unpack a tuple
name, age, city = ("Alice", 22, "Mumbai")
print(f"Name: {name}, Age: {age}, City: {city}")

# Nested tuple
nested = ((1, 2), (3, 4), (5, 6))
print(f"nested[1][0]: {nested[1][0]}")

# Convert list to tuple and back
lst = [10, 20, 30]
tup = tuple(lst)
back_to_list = list(tup)
print(f"List to tuple: {tup}, Back to list: {back_to_list}")

# Single element tuple (note the trailing comma)
single = (42,)
print(f"Single element tuple: {single}, Type: {type(single)}")

# Tuple with mixed types
mixed = (1, "hello", 3.14, True)
print(f"Mixed tuple: {mixed}")
