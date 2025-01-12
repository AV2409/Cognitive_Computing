# 8.1 
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")


# 8.2 
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input, please enter a number.")


# 8.3 
try:
    result = 5 / 0

except ZeroDivisionError:
    print("Cannot divide by zero.")

finally:
    print("This block executes no matter what.")

print()

try:
    result = 5 / 1

except ZeroDivisionError:
    print("Cannot divide by zero.")

finally:
    print("This block executes no matter what.")