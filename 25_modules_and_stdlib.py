# Modules and Standard Library in Python

# math module
import math

print(f"math.pi = {math.pi}")
print(f"math.e = {math.e}")
print(f"sqrt(144) = {math.sqrt(144)}")
print(f"ceil(4.2) = {math.ceil(4.2)}, floor(4.8) = {math.floor(4.8)}")
print(f"log(100, 10) = {math.log(100, 10)}")
print(f"sin(90 deg) = {math.sin(math.radians(90)):.2f}")

# random module
import random

print(f"\nrandom.random(): {random.random():.4f}")
print(f"random.randint(1, 10): {random.randint(1, 10)}")
items = ["apple", "banana", "cherry", "date"]
print(f"random.choice: {random.choice(items)}")
sample = random.sample(items, 2)
print(f"random.sample (2): {sample}")
random.shuffle(items)
print(f"Shuffled: {items}")

# datetime module
from datetime import datetime, date, timedelta

now = datetime.now()
print(f"\nCurrent datetime: {now.strftime('%Y-%m-%d %H:%M:%S')}")
today = date.today()
print(f"Today: {today}")
birthday = date(2000, 6, 15)
age_days = (today - birthday).days
print(f"Days since 2000-06-15: {age_days}")
tomorrow = today + timedelta(days=1)
print(f"Tomorrow: {tomorrow}")

# os module
import os

print(f"\nCurrent directory: {os.getcwd()}")
print(f"Home directory: {os.path.expanduser('~')}")
print(f"Path join: {os.path.join('folder', 'subfolder', 'file.txt')}")

# sys module
import sys

print(f"\nPython version: {sys.version.split()[0]}")
print(f"Platform: {sys.platform}")

# collections module
from collections import Counter, defaultdict, OrderedDict

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counter = Counter(words)
print(f"\nCounter: {counter}")
print(f"Most common: {counter.most_common(2)}")

dd = defaultdict(list)
dd["fruits"].append("apple")
dd["fruits"].append("banana")
dd["vegs"].append("carrot")
print(f"defaultdict: {dict(dd)}")
