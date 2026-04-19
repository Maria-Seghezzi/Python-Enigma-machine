class Plugboard:
    def __init__(self, connections: dict):
        self.connections = connections

    def encode(self, letter):
        if letter in self.connections:
            return self.connections[letter]
        else:
            return letter
