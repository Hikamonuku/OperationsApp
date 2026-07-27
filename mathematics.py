import math
import basic_operations

def select_math():
    while True:
        print("Math")
        print("Select the subarea you want to calculate: ")
        math_subarea = input("1. Basic Operations 2. Back: ")
        if math_subarea == "1" or math_subarea.lower() == "basic operations" or math_subarea.lower() == "operations":
            basic_operations.Select_Operation()
        elif math_subarea == "2" or math_subarea.lower() == "back":
            return
        else:
            print("Invalid option")