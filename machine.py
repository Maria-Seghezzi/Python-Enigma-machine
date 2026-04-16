from components import Rotor, Reflector


class Machine:
    def __init__(self, rotors: list[Rotor], reflector: Reflector):
        self.rotors = rotors
        self.reflector = reflector

    def encode(self, letter):
        """
        Encodes letter
        """
        enc_letter = letter

        print("Encoding forward")
        for rotor in self.rotors:
            enc_letter = rotor.encode_forward(enc_letter)
            print(enc_letter)

        print("going through reflector")
        enc_letter = self.reflector.encode(enc_letter)
        print(enc_letter)

        print("Encoding backwards")
        for rotor in reversed(self.rotors):
            enc_letter = rotor.encode_backward(enc_letter)
            print(enc_letter)
        return letter

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
                print(r.wiring[(r.current_position + x) % 26], end="")
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
