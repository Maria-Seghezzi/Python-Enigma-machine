from interface import parse_connections, parse_ref, parse_rotors
from machine import Machine
from machine import encode_message
import json
import copy

word = "HELLO"


# Defining configuration
def define_machine():
    with open("test\configuration.json", "r") as config_file:
        config_data = json.load(config_file)
        rotors_string = config_data["rotors"]
        ref_string = config_data["reflector"]
        plugboard_string = config_data["plugboard"]
    print(rotors_string, ref_string, plugboard_string)
    try:
        rotors = parse_rotors(rotors_string)
        ref = parse_ref(ref_string)
        plug = parse_connections(plugboard_string)
    except ValueError:
        print("Somthing wrong in configuration")
    else:
        machine = Machine(rotors, ref, plug)
    return machine


def test_simmetry(machine: Machine, file_path: str):
    enc_machine = machine
    dec_machine = copy.deepcopy(machine)
    with open(file_path, "r") as file:
        for string in file:
            word = string.replace("\r", "").replace("\n", "").upper()
            enc_message = encode_message(word, enc_machine)
            dec_message = encode_message(enc_message, dec_machine)
            assert word == dec_message


def test():
    machine = define_machine()
    test_simmetry(machine, "test\\test_cases.txt")


test()
