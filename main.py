from config.wiring_data import ROTORS_WIRINGS, REF_WIRING
from components.rotor import Rotor
from components.reflector import Reflector
from machine import Machine

# Future improvements:
# - Add notchs
# - Add plugboard

# TODO:
# Create function to print wirings
# Create function to let user encode multiple letters


def check_input_rotors(rotors):
    valid_input_name = ["I", "II", "III", "IV", "V"]
    if len(rotors) != 3:
        print("Failed len")
        return 0
    for r in rotors:
        if r[0].upper() not in valid_input_name:
            print(f"failed, {r} not in list {valid_input_name}")
            return 0
        valid_input_name.remove(r[0])
        if int(r[1]) < 0 or int(r[1]) > 26:
            print("failed position")
            return 0
    return 1


def check_input_ref(ref):
    valid_input = ["A", "B", "C"]
    if ref.upper() not in valid_input:
        return 0
    return 1


def print_presentation():
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
    done = 0
    while not done:
        action = input(
            "r: view rotor and reflectors wirings\ns: select rotors and reflector\n"
        )
        if action.lower() == "r":
            pass
            # Print rotors
        if action.lower() == "s":

            # Get rotors
            rotors_s = input(
                "Insert rotors to use and initial positions separated by a comma (eg: I:0, II:1, III:0): "
            )
            rotors_n = rotors_s.replace(" ", "").split(
                ","
            )  # Removes white spaces and creates list
            rotors_n = list(r.split(":") for r in rotors_n)
            # Check input
            valid = 0
            while not valid:
                print(rotors_n)
                rotors_n = rotors_s.replace(" ", "").split(
                    ","
                )  # Removes white spaces and creates list
                rotors_n = list(r.split(":") for r in rotors_n)
                # Check input
                if not check_input_rotors(rotors_n):
                    rotors_s = input("Please insert a valid input: ")
                else:
                    valid = 1
            # Create list of Rotors
            rotors_obj = []
            for i, rotor in enumerate(rotors_n):
                rotation_freq = 1 if i == 1 else 26 * i
                wiring = ROTORS_WIRINGS[rotor[0]]
                position = int(rotor[1])
                rotors_obj.append(Rotor(wiring, position, rotation_freq))

            # Get reflector
            ref_s = input("Insert reflector to use (A, B or C): ").upper()
            valid = 0
            # Check input
            while not valid:
                if not check_input_ref(ref_s):
                    ref_s = input("Please insert a valid input")
                else:
                    valid = 1
            # Create Reflector
            wiring = REF_WIRING[ref_s]
            ref_obj = Reflector(wiring)

            # Initializing machine
            enigma = Machine(rotors_obj, ref_obj)
            print("Machine created!")
            done = 1
            return enigma


def main():
    print_presentation()
    input("Press enter to enter configuration mode")
    enigma = configuration()
    print(enigma.encode("A"))


main()
