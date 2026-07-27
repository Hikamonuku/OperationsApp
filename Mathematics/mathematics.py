import math
import Mathematics.Arithmetic.arithmetic as arithmetic

def select_math():
    while True:
        print("Math")
        print("Select the subarea you want to calculate: ")
        math_subarea = input("1. Arithmetic 2. Back: ")
        if math_subarea == "1" or math_subarea.lower() == "arithmetic":
            arithmetic.select_arithmetics()
        elif math_subarea == "2" or math_subarea.lower() == "back":
            return
        else:
            print("Invalid option")