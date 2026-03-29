# Set Operations in Python

# Create a set (unordered, no duplicates)
fruits = {"apple", "banana", "cherry", "apple"}
print(f"Set (duplicates removed): {fruits}")

# Add and Remove
fruits.add("date")
fruits.discard("banana")
print(f"After add and discard: {fruits}")

# Check membership
print(f"'apple' in fruits: {'apple' in fruits}")

# Set from a list
nums = set([1, 2, 2, 3, 3, 4])
print(f"Set from list: {nums}")

# Set operations
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(f"Union (a | b): {a | b}")
print(f"Intersection (a & b): {a & b}")
print(f"Difference (a - b): {a - b}")
print(f"Symmetric Difference (a ^ b): {a ^ b}")

# Subset and Superset
x = {1, 2, 3}
y = {1, 2, 3, 4, 5}
print(f"x is subset of y: {x.issubset(y)}")
print(f"y is superset of x: {y.issuperset(x)}")

# Disjoint sets (no common elements)
p = {1, 2, 3}
q = {4, 5, 6}
print(f"p and q are disjoint: {p.isdisjoint(q)}")

# Frozenset (immutable set)
fs = frozenset([1, 2, 3])
print(f"Frozenset: {fs}, Type: {type(fs)}")

# Length
print(f"Length of set a: {len(a)}")
