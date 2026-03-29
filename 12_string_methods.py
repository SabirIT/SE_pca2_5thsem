# String Methods in Python

s = "Hello, World!"

# Length
print(f"Length: {len(s)}")

# Upper and Lower case
print(f"Upper: {s.upper()}")
print(f"Lower: {s.lower()}")

# Strip whitespace
s2 = "   spaces   "
print(f"Stripped: '{s2.strip()}'")

# Replace
print(f"Replace: {s.replace('World', 'Python')}")

# Split
csv = "apple,banana,cherry"
fruits = csv.split(",")
print(f"Split: {fruits}")

# Join
joined = " - ".join(fruits)
print(f"Joined: {joined}")

# Find and Index
print(f"Find 'World': {s.find('World')}")

# Starts with / Ends with
print(f"Starts with 'Hello': {s.startswith('Hello')}")
print(f"Ends with '!': {s.endswith('!')}")

# Count occurrences
print(f"Count 'l': {s.count('l')}")

# String slicing
print(f"Slice [0:5]: {s[0:5]}")
print(f"Reverse: {s[::-1]}")

# Check string content
print(f"'123'.isdigit(): {'123'.isdigit()}")
print(f"'abc'.isalpha(): {'abc'.isalpha()}")
print(f"'abc123'.isalnum(): {'abc123'.isalnum()}")

# Format string
person = "Alice"
score = 95.5
print(f"{person} scored {score:.1f} marks.")
