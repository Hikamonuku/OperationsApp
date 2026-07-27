import math
from .Mechanics import mechanics

def select_physics():
    print("Physics")
    while True: 
        print("Select the subarea you want to calculate: ")
        physics_subarea = input("1. Mechanics 2. Thermodynamics 3. Electronics 4. Optics 5. Waves 6. Modern Physics 7. Back: ")
        if physics_subarea == "1" or physics_subarea.lower() == "mechanics":
            mechanics.mechanics_branch()
        elif physics_subarea == "2" or physics_subarea.lower() == "thermodynamics":
            pass
        elif physics_subarea == "3" or physics_subarea.lower() == "electronics":
            pass
        elif physics_subarea == "4" or physics_subarea.lower() == "optics":
            pass
        elif physics_subarea == "5"or physics_subarea.lower() == "waves":
            pass
        elif physics_subarea == "6" or physics_subarea.lower() == "modern physics":
            pass
        elif physics_subarea == "7" or physics_subarea.lower() == "back":
            return
        else:
            return