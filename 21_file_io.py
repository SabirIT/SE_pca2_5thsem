# File I/O in Python
import os

filename = "sample.txt"

# Writing to a file
with open(filename, "w") as f:
    f.write("Line 1: Hello, Python!\n")
    f.write("Line 2: File I/O is easy.\n")
    f.write("Line 3: Always close your files.\n")
print(f"Written to '{filename}'")

# Reading entire file
with open(filename, "r") as f:
    content = f.read()
print(f"Full content:\n{content}")

# Reading line by line
with open(filename, "r") as f:
    lines = f.readlines()
print(f"Number of lines: {len(lines)}")
for i, line in enumerate(lines, 1):
    print(f"  Line {i}: {line.rstrip()}")

# Appending to a file
with open(filename, "a") as f:
    f.write("Line 4: Appended line.\n")
print("Appended a new line.")

# Reading with iteration
with open(filename, "r") as f:
    for line in f:
        print(f"  > {line.rstrip()}")

# Check if file exists
print(f"File exists: {os.path.exists(filename)}")
print(f"File size: {os.path.getsize(filename)} bytes")

# Rename and remove
os.rename(filename, "renamed_sample.txt")
print("File renamed to 'renamed_sample.txt'")

os.remove("renamed_sample.txt")
print("File 'renamed_sample.txt' deleted.")

# Working with directories
os.makedirs("test_dir/sub_dir", exist_ok=True)
print(f"Directories created: test_dir/sub_dir")
os.removedirs("test_dir/sub_dir")
print("Directories removed.")
