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
                if time == 0:
                    print("The Time interval cannot be zero")
                    continue
                print("Δt =", final_time, " - ", init_time)
                result = position / time
                print("V = ΔX / Δt", )
                print("V =", position, " / ", time)
                print("V = ", result)
            elif velocity_calc == "2":
                position = float(input("Insert the value of the Position: "))
                time = float(input("Insert the value of the Time: "))
                if time == 0:
                    print("The Time interval cannot be zero")
                    continue
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
                print("Xo = Xf - V * Δt")
                print("Xo = Xf - V * (t - to)")
                print("Xo = ", final_pos, " - ", velocity, "*", "(", final_time, " - ", init_time, ")")
                print("Xo = ", final_pos, " - ", velocity_time)
                result = final_pos - velocity_time
                print("Xo: ", result)
            elif position_calc == "2":
                final_pos = float(input("Final Position: "))
                velocity = float(input("Velocity: "))
                time = float(input("Time: "))
                if time == 0:
                    print("The Time interval cannot be zero")
                    continue
                velocity_time = velocity * time
                print("Xo = Xf - V * Δt")
                print("Xo = ", final_pos, " - ", velocity, " * ", time )
                print("Xo = ", final_pos, " - ", velocity_time)
                result = final_pos - velocity_time
                print("Xo = ", result)
            elif position_calc == "3":
                init_pos = float(input("Initial Position: "))
                velocity = float(input("Velocity: "))
                init_time = float(input("Initial Time: "))
                final_time = float(input("Final Time: "))
                delta_time = final_time - init_time
                if delta_time == 0:
                    print("The time interval cannot be zero")
                    continue
                velocity_time = velocity * delta_time
                print("Xf = Xo + V * Δt")
                print("Xf = ", init_pos, " + ", "(", velocity, " + ", "(", final_time, " - ", init_time, ")")
                print("Xf = ", init_pos, " + ", velocity_time)
                result = init_pos + velocity_time
                print("Xf = ", result)
            elif position_calc == "4":
                init_pos = float(input("Initial Position: "))
                velocity = float(input("Velocity: "))
                time = float(input("Time: "))
                if time == 0:
                    print("The time interval cannot be zero")
                    continue
                velocity_time = velocity * time
                print ("Xf = Xo + V * Δt")
                print("Xf = ", init_pos, " + ", velocity, " * ", time)
                result = init_pos + velocity_time
                print("Xf = ", result)
            elif position_calc == "5":
                print("ΔX = Xf - Xo")
                init_pos = float(input("Initial Position: "))
                final_pos = float(input("Final Position: "))
                delta_position = final_pos - init_pos
                print("ΔX = ", final_pos, " - ", init_pos)
                print("ΔX = ", delta_position)
            elif position_calc == "6":
                velocity = float(input("Insert the value of the Velocity: "))
                time = float(input("Insert the value of the Time: "))
                result = velocity * time
                print(velocity, " * ", time)
                print("X = ", result)
            else:
                print("Invalid option.")
        elif unit.lower() == "t" or unit == "3" or unit.lower() == "time":
            print("1. Initial Time: from Final Time, Velocity, Initial Position and Final Position")
            print("2. Initial Time: from Final Time, velocity and Position")
            print("3. Final Time: from Initial Time, Velocity and Initial Position and Final Position")
            print("4. Final Time: from Initial Time, Velocity and Position")
            print("5. Time Variation: from Final Time and Initial Time")
            print("6. Time: from Position and velocity")
            print("7. Back")
            time_calc = input("Select what you do want to calculate: ")
            if time_calc == "1":
                final_time = float(input("Final Time: "))
                velocity = float(print("Velocity: "))
                init_pos = float(print("Initial Position: "))
                final_pos = float(print("Final Position: "))
            elif time_calc == "2":
                final_time = float(input("Final Time: "))
                velocity = float(print("Velocity: "))
                position = float(print("Position: "))
            elif time_calc == "3":
                init_time = float(input("Initial Time: "))
                velocity = float(print("Velocity: "))
                init_pos = float(print("Initial Position: "))
                final_pos = float(print("Final Position: "))                
            elif time_calc == "4":
                init_time = float(input("Initial Time: "))
                velocity = float(print("Velocity: "))
                position = float(print("Position: "))
            elif time_calc == "5":
                init_time = float(input("Initial Time: "))
                final_time = float(input("Final Time: "))
                delta_time = final_time - init_time
                if delta_time == 0:
                    print("The time interval cannot be zero")
                    continue
            elif time_calc == "6":
                position = float(input("Insert the value of the Position: "))
                velocity = float(input("Insert the value of the Velocity: "))
                result = velocity / position
                if result == 0:
                    print("The time interval cannot be zero")
                    continue
                print(result)
            elif unit == "7":
                return
        elif unit == "4" or unit.lower() == "back":
            return
        else:
            print("Invalid entrance.")