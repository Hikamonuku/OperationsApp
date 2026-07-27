print("Uniform Motion")

def select_unit():
    while True:
        print("Select the Unit to be calculated: ")
        unit = input("1. Velocity(V) 2. Position(X) 3. Time(Δt) 4. Back: ")
        if unit.lower() == "v" or unit == "1" or unit.lower() == "velocity" or unit.lower() == "speed":
            print("Velocity Selected: ")
            print("1. Velocity: from Initial Position, Final Position, Initial Time and Final Time")
            print("2. Velocity: from Position and Time")
            print("3. Back")
            velocity_calc = input("Select what you do want to calculate: ")
            if velocity_calc == "1":
                init_pos = float(input("Initial Position: "))
                final_pos = float(input("Final Position: "))
                init_time = float(input("Initial Time: "))
                final_time = float(input("Final Time: "))
                print("calculations: ")
                position = final_pos - init_pos
                print("ΔX = ", final_pos, " - ", init_pos)
                time = final_time - init_time
                print("Δt =", final_time, " - ", init_time)
                result = position / time
                print("V = ΔX / ΔT", )
                print("V =", position, " / ", time)
                print("V = ", result)
            elif velocity_calc == "2":
                position = float(input("Insert the value of the Position: "))
                time = float(input("Insert the value of the Time: "))
                result = position / time
                print("V = ΔX / Δt")
                print(position, " / ", time)
                print("Result: ", result)
            elif velocity_calc == "3" or velocity_calc == "back":
                return
            else:
                print("Invalid option")
        elif unit.lower() == "x" or unit == "2" or unit.lower() == "position":
            print("Select what do you want to calculate in Position: ")
            print("1. Initial Position: from Final Position, velocity, Initial Time and Final Time")
            print("2. Initial Position: from Final Position, Velocity and Time")
            print("3. Final Position: from Initial Position, Velocity, Initial Time and Final Time")
            print("4. Final Position: from Initial Position, Velocity and Time")
            print("5. Position Variation: from Final Position and Initial Position")
            print("6. Position: from Velocity and Time")
            print("7. Back")
            position_calc = input("Select what you do want to calculate: ")
            if position_calc == "1":
                final_pos = float(input("Final Position: "))
                velocity = float(input("Velocity: "))
                init_time = float(input("Initial Time: "))
                final_time = float(input("Final Time: "))
                delta_time = final_time - init_time
                if delta_time == 0:
                    print("The time interval cannot be zero")
                    continue
                velocity_time = velocity * delta_time
                print("Xo = X - V * Δt")
                print("Xo = X - V * (t - to)")
                print("Xo = ", final_pos, " - ", velocity, "*", "(", final_time, " - ", init_time, ")")
                print("Xo = ", final_pos, " - ", velocity_time)
                result = final_pos - velocity_time
                print("Xo: ", result)
            elif position_calc == "2":
                final_pos = float(input("Final Position: "))
                velocity = float(input("Velocity: "))
                time = float(input("Time: "))
                velocity_time = velocity * time
                print("X = Xo - V * Δt")
                print("X = ", final_pos, " - ", velocity, " * ", time )
                print("X = ", final_pos, " - ", velocity_time)
                result = final_pos - velocity_time
                print("X = ", result)
            elif position_calc == "3":
                pass
            elif position_calc == "6":
                velocity = float(input("Insert the value of the Velocity: "))
                time = float(input("Insert the value of the Time: "))
                result = velocity * time
                print(velocity, " * ", time)
                print(result)
        elif unit.lower() == "t" or unit == "3" or unit.lower() == "time":
            print("1. Initial Time: from Final Time, Velocity and Position")
            print("2. Final Time: from Initial Time, Velocity and Position")
            print("3. Time Variation: from Final Time and Initial Time")
            print("4. Time: from Position and velocity")
            print("5. Back")
            time_calc = input("Select what you do want to calculate: ")
            if time_calc == "2":
                init_time = float(input("Initial Time: "))
                velocity = float(input("Velocity: "))
                position = float(input("Position: "))

            if time_calc == "4":
                position = float(input("Insert the value of the Position: "))
                velocity = float(input("Insert the value of the Velocity"))
                result = velocity / position
                print(result)
            elif unit == "5":
                return
        elif unit == "4" or unit.lower() == "back":
            return
        else:
            print("Invalid entrance.")
