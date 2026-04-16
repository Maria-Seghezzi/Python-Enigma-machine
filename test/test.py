# from components.rotor import Rotor
from components.reflector import Reflector
from config.wiring_data import *

word = "HELLO"

ref = Reflector(WIRING_R_A)

enc_word = ""

for letter in word:
    l = ref.encode(letter)
    print(l)
    enc_word += l
