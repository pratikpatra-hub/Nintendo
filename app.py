import sys

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def multi(num1, num2):
    return num1 * num2

def div(num1, num2):
    if num2 == 0:
        return "Error: Division by zero"
    return num1 / num2

# Reading inputs from command-line arguments
num1 = int(sys.argv[1])
operation = sys.argv[2]
num2 = int(sys.argv[3])

# Performing the calculation
if operation == "+":
    result = add(num1, num2)
elif operation == "-":
    result = sub(num1, num2)
elif operation == "*":
    result = multi(num1, num2)
elif operation == "/":
    result = div(num1, num2)
else:
    result = "Invalid operation"

# Printing the result
print("Result:", result)

