# Dictionary Operations in Python

# Create a dictionary
student = {"name": "Alice", "age": 21, "grade": "A"}
print(f"Dictionary: {student}")

# Access values
print(f"Name: {student['name']}")
print(f"Age (get): {student.get('age')}")
print(f"Missing key (default): {student.get('score', 0)}")

# Add / Update key-value pairs
student["score"] = 95
student["age"] = 22
print(f"After update: {student}")

# Remove items
removed = student.pop("score")
print(f"Removed 'score': {removed}, Dict: {student}")

del student["grade"]
print(f"After del 'grade': {student}")

# Keys, Values, Items
info = {"a": 1, "b": 2, "c": 3}
print(f"Keys: {list(info.keys())}")
print(f"Values: {list(info.values())}")
print(f"Items: {list(info.items())}")

# Check membership
print(f"'a' in info: {'a' in info}")

# Iterate over dictionary
for key, value in info.items():
    print(f"  {key}: {value}")

# Dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

# Merge two dictionaries
dict1 = {"x": 1, "y": 2}
dict2 = {"y": 99, "z": 3}
merged = {**dict1, **dict2}
print(f"Merged: {merged}")

# Nested dictionary
school = {
    "student1": {"name": "Bob", "marks": 85},
    "student2": {"name": "Carol", "marks": 92},
}
print(f"student2 marks: {school['student2']['marks']}")
