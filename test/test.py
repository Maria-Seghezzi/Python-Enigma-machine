from components.rotor import Rotor
from components.reflector import Reflector
from config.wiring_data import *
from machine import Machine

word = "HELLO"

# Defining configuration
rotors = [Rotor(WIRING_I, 0, 1), Rotor(WIRING_II, 0, 0), Rotor(WIRING_III, 0, 0)]
ref = Reflector(WIRING_R_A)

# Test encoding
m = Machine(rotors, ref)
m.print_components(rotors=[1, 2])
m.encode("A")
m.print_components(rotors=[1, 2])
m.encode("A")
