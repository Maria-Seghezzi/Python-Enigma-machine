from interface import get_configuration
from machine import encode_message

# Future improvements:
# - Add notchs


def print_presentation():
    """
    Print presentation
    """
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


def main():
    print_presentation()
    input("Press enter to enter configuration mode")
    enigma = get_configuration()
    message = input("Enter message to encode or decode: ")
    encoded_message = encode_message(message, enigma)
    print("Encoded message:", encoded_message)


if __name__ == "__main__":
    main()
