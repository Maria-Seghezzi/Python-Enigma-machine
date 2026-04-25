from components import Rotor, Reflector, Plugboard
from config.wiring_data import ROTORS_WIRINGS, REF_WIRING
from machine import Machine


def parse_connections(connection_string):
    """
    Check if input contains valid plugboard connections and return Plugboard object
    """
    connection_string = connection_string.upper()
    # Remove spaces and create list
    connections_list = connection_string.replace(" ", "").split(",")
    # Create connection dict
    connections = {}
    # Parse input if it isn't empty
    if connections:
        for connection in connections_list:
            if ":" not in connection:
                raise ValueError
            a, b = connection.split(":")
            a, b = a.upper(), b.upper()
            if a in connections or b in connections or a == b:
                raise ValueError
            connections[a] = b
            connections[b] = a
    # Create Plugboard object
    plugboard_obj = Plugboard(connections)

    return plugboard_obj


def parse_ref(ref_string):
    """
    Check if input contains valid reflector name and returns reflector object
    """
    ref_string = ref_string.upper()
    # Check if input is valid
    valid_input = ["A", "B", "C"]
    if ref_string not in valid_input:
        raise ValueError
    # Create Reflector
    wiring = REF_WIRING[ref_string]
    ref_obj = Reflector(wiring)
    return ref_obj


def parse_rotors(rotors_string):
    """
    Check if input contains valid rotors names and positions and returns list of Rotor objects
    """
    valid_input_name = ["I", "II", "III", "IV", "V"]

    rotors_string = rotors_string.upper()
    # Remove spaces and create list
    rotors = rotors_string.replace(" ", "").split(",")
    # Create rotors list
    rotors_list = []
    for r in rotors:
        if ":" not in r:
            raise ValueError
        rotors_list.append(r.split(":"))

    # Check length
    if len(rotors_list) != 3:
        raise ValueError
    # Check if elements are valid names and position, and that there are no duplicates
    for r in rotors_list:
        if r[0] not in valid_input_name:
            raise ValueError
        valid_input_name.remove(r[0])
        if int(r[1]) < 0 or int(r[1]) > 26:
            raise ValueError

    # Create list of Rotor objects
    rotors_obj = []
    for i, r in enumerate(rotors_list):
        rotation_freq = 1 if i == 0 else 26 * i
        wiring = ROTORS_WIRINGS[r[0]]
        position = int(r[1])
        rotors_obj.append(Rotor(wiring, position, rotation_freq))
    return rotors_obj


def get_configuration():
    """
    Ask user to define the machine configuration
    """

    # Get rotors
    rotors_s = input(
        "Insert rotors to use and initial positions separated by a comma (eg: I:0, II:1, III:0): "
    )
    while True:
        try:
            rotors_obj = parse_rotors(rotors_s)
            break
        except ValueError:
            rotors_s = input("Please insert a valid input: ")

    # Get reflector
    ref_s = input("Insert reflector to use (A, B or C): ").upper()
    while True:
        try:
            ref_obj = parse_ref(ref_s)
            break
        except ValueError:
            ref_s = input("Please insert a valid input: ").upper()

    # Get plugboard connections
    plug_s = input("Insert plugboard connections separated by a comma (eg A:B, C:D)")
    while True:
        try:
            plugboard_obj = parse_connections(plug_s)
            break
        except ValueError:
            plug_s = input("Please insert a valid input: ")

    # Initializing machine
    enigma = Machine(rotors_obj, ref_obj, plugboard_obj)
    print("Machine created!")
    return enigma
