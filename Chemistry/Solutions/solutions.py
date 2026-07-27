import math

def select_calculation():
    while True:
        print("Select what you do want to calculate: ")
        operation = input("1. Density 2. Dilution 3. Concentration 4. Molality 5. Molarity(M) 6. Moles(n) 7. Volume(V) 8. Back: ")
        if operation == "8" or operation.lower() == "back":
            return
        else:
            print("Invalid option")