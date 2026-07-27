import math

def select_option():
    while True:
        print("Select what you do want to calculate: ")
        print("1. Number of Protons ")
        print("2. Number of Electrons")
        print("3. Number of Neutrons")
        print("4. Atomic Number ")
        print("5. Mass Number")
        print("6. Ion Charge")
        operation = input("7. Back")
        if operation == "1" or operation.lower() == "protons":
            pass
        elif operation == "2" or operation.lower() == "electrons":
            pass
        elif operation == "3" or operation.lower() == "neutrons":
            pass
        elif operation == "4" or operation.lower() == "atomic":
            pass
        elif operation == "5" or operation.lower() == "mass":
            pass
        elif operation == "6" or operation.lower() == "ion" or operation.lower("charge") or operation.lower() == "ion charge":
            pass
        elif operation == "7" or operation.lower() == "back":
            return
