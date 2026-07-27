import math
from . import basic_operations

print("Arithmetic")

def select_arithmetics():
    while True:
        print("Select a module: ")
        arithmetics_module = input("1. Basic Operations 2. Back: ")
        if arithmetics_module == "1" or arithmetics_module.lower() == "basic operations" or arithmetics_module.lower() == "operations":
            basic_operations.select_operation()
        else:
            print("Invalid option. Please select an option")
            return