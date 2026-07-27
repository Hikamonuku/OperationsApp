import Chemistry.chemistry as chemistry
import Mathematics.mathematics as mathematics
import Physics.physics as physics

def select_subject():
    while True:
        print("Welcome to the OperationsApp")
        print("Select a subject: ")
        subject = input("1. Chemistry 2. Math 3. Physics 4.Close: ")
        if subject.lower() == "1" or subject.lower() == "chemistry" or subject.lower() == "chem":
            chemistry.select_chemistry()
        elif subject.lower() == "2" or subject.lower() == "math" or subject.lower() == "mathematics":
            mathematics.select_math()
        elif subject.lower() == "3" or subject.lower() == "physics" or subject.lower() == "physic":
            physics.select_physics()
        elif subject.lower() == "4" or subject.lower() == "close" or subject.lower() == "finish":
            return
        else:
            print("Invalid Subject.")

select_subject()