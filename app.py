# Define functions for each operation
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Define a main function to perform the operation
def perform_operation():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            operator = input("Enter the operation (+, -, *, /): ")
            num2 = float(input("Enter the second number: "))
    
            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
            else:
                print("Invalid operator")
                continue  # Restart the loop
                
            print(f"Result: {num1} {operator} {num2} = {result}")
            
            repeat = input("Do you want to perform another calculation? (yes/no): ")
            if repeat.lower() != 'yes':
                break
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue  # Restart the loop

# Call the main function to start the calculation process
perform_operation()
