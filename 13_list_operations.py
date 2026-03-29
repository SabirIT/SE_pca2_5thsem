# List Operations in Python

# Create a list
fruits = ["apple", "banana", "cherry", "date"]
print(f"List: {fruits}")

# Access elements
print(f"First: {fruits[0]}, Last: {fruits[-1]}")

# Slicing
print(f"Slice [1:3]: {fruits[1:3]}")

# Append and Insert
fruits.append("elderberry")
fruits.insert(1, "avocado")
print(f"After append and insert: {fruits}")

# Remove elements
fruits.remove("date")
popped = fruits.pop()
print(f"After remove and pop: {fruits}, Popped: {popped}")

# Length, Min, Max
numbers = [5, 2, 8, 1, 9, 3]
print(f"Length: {len(numbers)}, Min: {min(numbers)}, Max: {max(numbers)}, Sum: {sum(numbers)}")

# Sort and Reverse
numbers.sort()
print(f"Sorted: {numbers}")
numbers.reverse()
print(f"Reversed: {numbers}")

# Check membership
print(f"8 in numbers: {8 in numbers}")

# Concatenate lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(f"Combined: {combined}")

# Count and Index
nums = [1, 2, 2, 3, 2, 4]
print(f"Count of 2: {nums.count(2)}, Index of 3: {nums.index(3)}")

# Copy a list
original = [1, 2, 3]
copy = original.copy()
copy.append(4)
print(f"Original: {original}, Copy: {copy}")

# Nested list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Matrix[1][2]: {matrix[1][2]}")
