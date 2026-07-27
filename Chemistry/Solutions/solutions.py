import math

def select_calculation():
    while True:
        print("Select what you do want to calculate: ")
        operation = input("1. Density 2. Dilution 3. Concentration 4. Molality 5. Molarity(M) 6. Moles(n) 7. Title 8. Back: ")
        if operation == "1" or operation.lower == "density":
            print("1. Density(d) 2. Mass(m) 3. Volume(V) 4. Back")
            density_calculation = input("Select what you do want to calculate: ")
            if density_calculation == "1" or density_calculation.lower() == "density" or density_calculation.lower() == "d":
                mass = float(input("Mass: "))
                if mass == 0:
                    print("Mass cannot be zero")
                    continue
                volume = float(input("Volume: "))
                if volume == 0:
                    print("Volume cannot be zero.")
                    continue
                result = mass / volume
                print("Density: ", result)
            elif density_calculation == "2" or density_calculation.lower() == "mass" or density_calculation.lower() == "m":
                density = float(input("Density: "))
                if density == 0:
                    print("Density cannot be zero.")
                    continue
                volume = float(input("Volume: "))
                if volume == 0:
                    print("Volume cannot be zero")
                    continue
                result = density * volume
                print("Mass: ", result)
            elif density_calculation == "3" or density_calculation.lower() == "volume" or density_calculation.lower() == "v":
                density = float(input("Density: "))
                if density == 0:
                    print("Density cannot be zero")
                    continue
                mass = float(input("Mass: "))
                if mass == 0:
                    print("Mass cannot be zero")
                    continue
                result = mass / density
                print("Volume: ", result)
            elif density_calculation == "4" or density_calculation.lower() == "back":
                return
        elif operation == "2" or operation.lower() == "dilution":
            pass
        elif operation == "3" or operation.lower() == "concentration":
            pass
        elif operation == "4" or operation.lower() == "molality":
            pass
        elif operation == "5" or operation.lower() == "molarity":
            pass
        elif operation == "6" or operation.lower() == "mole" or operation.lower() == "moles":
            pass
        elif operation == "7" or operation.lower() == "title":
            pass
        elif operation == "8" or operation.lower() == "back":
            return
        else:
            print("Invalid option")