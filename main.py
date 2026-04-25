from interface import get_configuration
from machine import encode_message

# Future improvements:
# - Add notchs


def print_presentation():
    presentation = """ _____      _                         _____                _       _             
|  ___|    (_)                       |  ___|              | |     | |            
| |__ _ __  _  __ _ _ __ ___   __ _  | |__ _ __ ___  _   _| | __ _| |_ ___  _ __ 
|  __| '_ \| |/ _` | '_ ` _ \ / _` | |  __| '_ ` _ \| | | | |/ _` | __/ _ \| '__|
| |__| | | | | (_| | | | | | | (_| | | |__| | | | | | |_| | | (_| | || (_) | |   
\____/_| |_|_|\__, |_| |_| |_|\__,_| \____/_| |_| |_|\__,_|_|\__,_|\__\___/|_|   
               __/ |                                                             
              |___/                                                                                                                         """
    print(presentation, "\n\n")


def main():
    print_presentation()
    input("Press enter to enter configuration mode")
    enigma = get_configuration()
    message = input("Enter message to encode or decode or '\\' to exit: ")
    while message != "\\":
        encoded_message = encode_message(message, enigma)
        print("Encoded message:", encoded_message)
        message = input("Enter message to encode or decode or '\\' to exit: ")


if __name__ == "__main__":
    main()
