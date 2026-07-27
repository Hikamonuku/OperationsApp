print("Uniform Motion")

def select_unit():
    while True:
        print("Select the Unit to be calculated: ")
        unit = input("1. Velocity(V) 2. Distance(X) 3. Time(Δt) 4. Back: ")
        if unit.lower() == "v" or unit == "1" or unit.lower() == "velocity" or unit.lower() == "speed":
            distance = float(input("Insert the value of the Distance: "))
            time = float(input("Insert the value of the Time: "))
            result = distance / time
            print(result)
        elif unit.lower() == "x" or unit == "2" or unit.lower() == "distance":
            velocity = float(input("Insert the value of the Velocity: "))
            time = float(input("Insert the value of the Time: "))
            result = velocity * time
            print(result)
        elif unit.lower() == "t" or unit == "3" or unit.lower() == "time":
            distance = float(print("Insert the value of the Distance: "))
            velocity = float(print("Insert the value of the Velocity"))
            result = velocity / distance
            print(result)
        elif unit == "4":
            return
        else:
            print("Invalid entrance.")