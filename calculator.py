# Define the calculator function
def calculator():
    print("Simple Calculator")
    print("Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    # Prompt the user for operation choice
    choice = input("Enter operation (1/2/3/4): ")
    # Check if the choice is valid
    if choice not in ('1', '2', '3', '4'):
        print("Invalid input")
        return
    # Prompt the user for two numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    # Perform the calculation based on the user's choice
    if choice == '1':
        result = num1 + num2
        print("Result:", result)
    elif choice == '2':
        result = num1 - num2
        print("Result:", result)
    elif choice == '3':
        result = num1 * num2
        print("Result:", result)
    elif choice == '4':
        # Check for division by zero
        if num2 == 0:
            print("Error: Division by zero")
        else:
            result = num1 / num2
            print("Result:", result)


# Call the calculator function
calculator()
