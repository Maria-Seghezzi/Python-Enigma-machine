from components.rotor import Rotor
from components.reflector import Reflector
from config.wiring_data import *
from machine import Machine

word = "HELLO"

# Defining configuration
rotors = [Rotor(WIRING_I, 0, 0), Rotor(WIRING_I, 1, 0), Rotor(WIRING_I, 2, 0)]
ref = Reflector(WIRING_R_C)

# Test encoding
m = Machine(rotors, ref)
m.print_components()
print(m.encode("A"))
