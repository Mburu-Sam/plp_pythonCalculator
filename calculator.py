#Ask user to enter two numbers
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
#Ask user to choose an operation
operation = input("Choose an operation (+, -, *, /): ")
#Perform the operation based on user input
if operation == '+':        
    result = number1 + number2
elif operation == '-':
    result = number1 - number2
elif operation == '*':
    result = number1 * number2

elif operation == '/':
    if number2 != 0:
        result = number1 / number2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operation selected."
#Display the result
print(f"The result is: {result}")
