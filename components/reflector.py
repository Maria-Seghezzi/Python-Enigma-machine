class Reflector:

    def __init__(self, wiring: list):
        self.wiring = wiring

    def encode(self, letter: str):
        """
        Encodes letter, returns encoded letter (char)
        """
        letter_index = ord(letter) - 65
        return self.wiring[(letter_index)]
