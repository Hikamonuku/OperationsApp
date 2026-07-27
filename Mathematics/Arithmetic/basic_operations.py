print("Basic Operations")
import math

def select_operation():
    while True: 
        print("Select an Operation:")
        operation = input("1. Addition 2. Subtraction 3. Multiplication 4. Division 5. nTh Root 6. Exponentiation 7. Logarithm 8. Back: ").lower()
        if operation == "8" or operation.lower() == "back":
            return
        first_number = float(input("Select the first number: "))
        second_number = float(input("Select the second number: "))
        if operation == "1" or operation.lower() == "addition" or operation.lower() == "add":
            result = first_number + second_number
        elif operation == "2" or operation.lower() == "subtraction" or operation.lower() == "subtract":
            result = first_number - second_number
        elif operation == "3" or operation.lower() == "multiplication" or operation.lower() == "multiply":
            result = first_number * second_number
        elif operation == "4" or operation.lower() == "division" or operation.lower() == "divide":
            result = first_number / second_number
        elif operation == "5" or operation.lower() == "nth root" or operation.lower() == "root":
            result = first_number ** (1 / second_number)
        elif operation == "6" or operation.lower() == "exponentiation" or operation.lower() == "exponential":
            result = first_number ** second_number
        elif operation == "7" or operation.lower() == "logarithm" or operation.lower() == "log":
            result = math.log(first_number, second_number)
        else:
            print("Invalid option. Please select an option")
            continue
        print(result)