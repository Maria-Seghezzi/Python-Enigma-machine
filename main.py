from config.wiring_data import ROTORS_WIRINGS, REF_WIRING
from components import Rotor, Reflector, Plugboard
from machine import Machine

# Future improvements:
# - Add notchs
# - Add plugboard


def parse_rotors(rotors_string):
    """
    Check if input contains valid rotors names
    """
    valid_input_name = ["I", "II", "III", "IV", "V"]

    # Remove white spaces and create list
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
        if r[0].upper() not in valid_input_name:
            raise ValueError
        valid_input_name.remove(r[0])
        if int(r[1]) < 0 or int(r[1]) > 26:
            raise ValueError
    return rotors_list


def parse_ref(ref_string):
    """
    Check if input contains valid reflector name
    """
    valid_input = ["A", "B", "C"]
    if ref_string.upper() not in valid_input:
        raise ValueError
    return 1


def parse_connections(connection_string):
    connections_list = connection_string.replace(" ", "").split(",")
    connections = {}
    for connection in connections_list:
        if ":" not in connection:
            raise ValueError
        a, b = connection.split(":")
        a, b = a.upper(), b.upper()
        if a in connections or b in connections or a == b:
            raise ValueError
        connections[a] = b
        connections[b] = a
    return connections


def print_presentation():
    """
    Print presentation
    """
    presentation = "ENIGMA MACHINE EMULATOR"
    for j in range(2):
        for i in range(len(presentation) + 12):
            print("#", end="")
        print()
    for i in range(6):
        print("-", end="")
    print(presentation, end="")
    for i in range(6):
        print("-", end="")
    print()
    for j in range(2):
        for i in range(len(presentation) + 12):
            print("#", end="")
        print()
    print("\n")


def configuration():
    """
    Ask user to define the machine configuration
    """

    # Get rotors
    rotors_s = input(
        "Insert rotors to use and initial positions separated by a comma (eg: I:0, II:1, III:0): "
    )
    while True:
        try:
            rotors = parse_rotors(rotors_s)
            break
        except ValueError:
            rotors_s = input("Please insert a valid input: ")

    # Create list of rotor objects
    rotors_obj = []
    for i, rotor in enumerate(rotors):
        rotation_freq = 1 if i == 0 else 26 * i
        wiring = ROTORS_WIRINGS[rotor[0]]
        position = int(rotor[1])
        rotors_obj.append(Rotor(wiring, position, rotation_freq))

    # Get reflector
    ref_s = input("Insert reflector to use (A, B or C): ").upper()
    # Check input
    while True:
        try:
            parse_ref(ref_s)
            break
        except ValueError:
            ref_s = input("Please insert a valid input: ").upper()

    # Create Reflector
    wiring = REF_WIRING[ref_s]
    ref_obj = Reflector(wiring)

    # Get plugboard connections
    plug_s = input("Insert plugboard connections separated by a comma (eg A:B, C:D)")
    while True:
        try:
            connections = parse_connections(plug_s)
            break
        except ValueError:
            plug_s = input("Please insert a valid input: ")
    # Create plugboard object
    plugboard = Plugboard(connections)

    # Initializing machine
    enigma = Machine(rotors_obj, ref_obj, plugboard)
    print("Machine created!")
    done = 1
    return enigma


def encode_message(message: str, machine: Machine):
    message = message.upper()
    enc_message = ""
    for letter in message:
        if letter.isalpha():
            enc_message += machine.encode(letter)
        else:
            enc_message += letter
    return enc_message


def main():
    print_presentation()
    input("Press enter to enter configuration mode")
    enigma = configuration()
    message = input("Enter message to encode or decode: ")
    encoded_message = encode_message(message, enigma)
    print("Encoded message:", encoded_message)


main()
