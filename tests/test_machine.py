from interface import parse_connections, parse_ref, parse_rotors
from machine import Machine
from machine import encode_message
import json
import copy


# Defining configuration
def define_machine(configuration_file):
    with open(configuration_file, "r") as config_file:
        config_data = json.load(config_file)
        rotors_string = config_data["rotors"]
        ref_string = config_data["reflector"]
        plugboard_string = config_data["plugboard"]
    try:
        rotors = parse_rotors(rotors_string)
        ref = parse_ref(ref_string)
        plug = parse_connections(plugboard_string)

        return Machine(rotors, ref, plug)

    except (ValueError, KeyError, json.JSONDecodeError) as e:
        raise ValueError(f"Invalid configuration file: {e}")


def test_simmetry():
    machine = define_machine("tests/configuration.json")

    enc_machine = machine
    dec_machine = copy.deepcopy(machine)

    with open("tests/test_cases.txt", "r") as file:
        for string in file:
            word = string.replace("\r", "").replace("\n", "").upper()
            enc_message = encode_message(word, enc_machine)
            dec_message = encode_message(enc_message, dec_machine)

            assert word == dec_message
