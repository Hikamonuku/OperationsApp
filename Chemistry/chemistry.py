import math
from .Solutions import solutions

def select_chemistry():
    while True:
        print ("Chemistry")
        print("Select the subarea you want to calculate: ")
        chem_subarea = input("1. Atomistic 2. Solutions 3. Stoichometry 4. Back: ")
        if chem_subarea == "1" or chem_subarea.lower() == "Atomistic":
            pass
        elif chem_subarea == "2" or chem_subarea.lower() == "solutions":
            solutions.select_calculation()
        elif chem_subarea == "3" or chem_subarea.lower == "stoichometry":
            pass
        elif chem_subarea == "4" or chem_subarea.lower == "back":
            return