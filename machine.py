from components import Rotor, Reflector, Plugboard


class Machine:
    def __init__(self, rotors: list[Rotor], reflector: Reflector, plugboard: Plugboard):
        self.rotors = rotors
        self.reflector = reflector
        self.plugboard = plugboard
        self.letter_count = 0

    def update(self):
        """
        Updates rotors positions
        """
        for rotor in self.rotors:
            rotor.update(self.letter_count)

    def encode(self, letter):
        """
        Encodes letter
        """
        self.letter_count += 1
        enc_letter = letter

        # Plugboard
        enc_letter = self.plugboard.encode(enc_letter)

        # Encode forward
        for rotor in self.rotors:
            enc_letter = rotor.encode_forward(enc_letter)

        # Reflector
        enc_letter = self.reflector.encode(enc_letter)

        # Encode backwards
        for rotor in reversed(self.rotors):
            enc_letter = rotor.encode_backward(enc_letter)

        # Plugboard
        enc_letter = self.plugboard.encode(enc_letter)

        self.update()
        return enc_letter

    def print_components(self, rotors=[1, 2, 3], reflector=1):
        """
        Prints internal wiring of components of the machine, based on current position
        """
        # Print rotors
        for j in rotors:
            r = self.rotors[j - 1]
            print(f"ROTOR {j}")
            # Print alphabet
            for i in range(26):
                print(chr(i + 65), end="")
            print("")
            # Print wiring
            for x in range(26):
                letter = chr(x + 65)
                print(r.encode_forward(letter), end="")
            print("\n")

        # Print reflector
        if reflector:
            print("REFLECTOR")
            # Print alphabet
            for i in range(26):
                print(chr(i + 65), end="")
            print("")
            # Print wiring
            for l in self.reflector.wiring:
                print(l, end="")
        print("\n")


def encode_message(message: str, machine: Machine):
    message = message.upper()
    enc_message = ""
    for letter in message:
        if letter.isalpha():
            enc_message += machine.encode(letter)
        else:
            enc_message += letter
    return enc_message
