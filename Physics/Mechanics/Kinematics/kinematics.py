import math
from . import uniform_motion
from . import accelerated_motion

print("Kinematics")

def select_kinematics():
    while True:
        print("Select one module: ")
        kinematics_module = input("1. Uniform Motion 2. Uniformly Accelerated Motion 3. Free Fall 4. Projectile Motion 5. Back: ")
        if kinematics_module == "1" or kinematics_module.lower() == "uniform motion" or kinematics_module.lower() == "UM" or kinematics_module.lower() == "uniform motion":
            uniform_motion.select_unit()
        elif kinematics_module == "2" or kinematics_module.lower() == "uniformly accelerated motion" or kinematics_module.lower() == "accelerated motion" or kinematics_module.lower() == "am":
            accelerated_motion.select_unit()
        elif kinematics_module == "3" or kinematics_module.lower() == "free fall" or kinematics_module.lower() == "fall":
            pass
        elif kinematics_module == "4" or kinematics_module.lower() == "projectile motion" or kinematics_module.lower() == "projectile":
            pass
        elif kinematics_module == "5" or kinematics_module.lower() == "back":
            return
        else:
            print("Invalid option. ")
