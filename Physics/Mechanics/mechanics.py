import math
from .Kinematics import kinematics

def mechanics_branch():
    while True:
        print("Select the Module: ")
        kinematics_module = input("1. Kinematics 2. Dynamics 3. Gravitation 4. Work and Energy 5. Momentum 6. Back: ")
        if kinematics_module == "1" or kinematics_module.lower() == "kinematics":
            kinematics.select_kinematics()
        elif kinematics_module == "2" or kinematics_module.lower() == "dynamics":
            pass
        elif kinematics_module == "3" or kinematics_module.lower() == "gravitation":
            pass
        elif kinematics_module == "4" or kinematics_module.lower() == "work" or kinematics_module.lower == "energy" or kinematics_module.lower() == "work and energy":
            pass
        elif kinematics_module == "5" or kinematics_module.lower() == "momentum":
            pass
        elif kinematics_module == "6" or kinematics_module.lower() == "back":
            return
        else:
            print("Invalid option. ")