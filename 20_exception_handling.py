# Exception Handling in Python

# Basic try-except
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Caught ZeroDivisionError: {e}")

# Multiple exceptions
def safe_convert(value):
    try:
        return int(value)
    except ValueError:
        print(f"Cannot convert '{value}' to int")
    except TypeError:
        print(f"Invalid type: {type(value)}")
    return None

print(safe_convert("42"))
print(safe_convert("abc"))
print(safe_convert(None))

# else block (runs when no exception occurs)
try:
    num = int("100")
except ValueError:
    print("Conversion failed")
else:
    print(f"Conversion succeeded: {num}")

# finally block (always runs)
try:
    data = [1, 2, 3]
    print(data[10])
except IndexError as e:
    print(f"IndexError: {e}")
finally:
    print("Finally block always executes")

# Raising exceptions
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age is unrealistically high")
    return f"Valid age: {age}"

try:
    print(check_age(25))
    print(check_age(-5))
except ValueError as e:
    print(f"ValueError: {e}")

# Custom exception
class InsufficientFundsError(Exception):
    def __init__(self, amount, balance):
        self.amount = amount
        self.balance = balance
        super().__init__(f"Cannot withdraw {amount}. Balance is {balance}.")

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(amount, balance)
    return balance - amount

try:
    new_balance = withdraw(100, 150)
except InsufficientFundsError as e:
    print(f"Custom Exception: {e}")
