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
        return self.wiring[(self.current_position + letter_index) % 26]

    def encode_backward(self, letter: str):
        """
        Encodes letter backward, returns encoded letter (char)
        """
        letter_index = ord(letter) - 65
        out_letter_index = self.wiring.index(letter_index)
        return chr(out_letter_index + 65)
