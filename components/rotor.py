class Rotor:
    def __init__(self, wiring: list, initial_position: int, rotation_freq: int):
        self.wiring = wiring
        self.initial_position = initial_position
        self.rotation_freq = rotation_freq
        self.current_position = initial_position

    def update(self, letter_count: int):
        """
        Updates rotor state
        """
        if self.rotation_freq == 0:
            return
        if letter_count % self.rotation_freq == 0:
            self.current_position += 1

    def encode_forward(self, letter: str):
        """
        Encodes letter forward, returns encoded letter (char)
        """
        letter_index = ord(letter) - 65
        # Take index of the letter that enters the rotor (shift)
        index_letter_in = (self.current_position + letter_index) % 26
        # Calculate index of letter that exits the rotor (unshift)
        index_letter_out = (
            ord(self.wiring[index_letter_in]) - 65 - self.current_position
        ) % 26

        return chr(index_letter_out + 65)

    def encode_backward(self, letter: str):
        """
        Encodes letter backward, returns encoded letter (char)
        """
        # Take index of letter that enters the rotor
        shifted_letter_index = (ord(letter) - 65 + self.current_position) % 26
        in_letter = chr(shifted_letter_index + 65)
        # Calculate index of letter that exits the rotor
        mapped_index = self.wiring.index(in_letter)
        out_letter_index = (mapped_index - self.current_position) % 26 + 65

        return chr(out_letter_index)
