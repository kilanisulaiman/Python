print("Hello, World!")

name = input("What is your name? ")

print(f"Nice to meet you, {name}!")

print("Let's do a simple math operation.")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose an operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2

print(f"The result is: {result}")
