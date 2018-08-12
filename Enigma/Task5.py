from Rotor import Rotor
from Enigma import Enigma
from Plugboard import Plugboard

rotors = ["EKMFLGDQVZNTOWYHXUSPAIBRCJ", "AJDKSIRUXBLHWTMCQGZNPYFVOE", "BDFHJLCPRTXVZNYEIWGAKMUSQO",
          "ESOVPZJAYQUIRHXLNFTGKDCMWB", "VZBRGITYUPSDNHLXAWMJQOFECK"]

def string_to_dict(letters_dict):
    """
    create dictionary from string.
    :param letters_dict: string.
    :return: dictionary.
    """
    _dict = dict()

    for key, value in enumerate(letters_dict):
        _dict[key] = value

    return _dict

def letter_to_index(letter):
    """
    Translate index to char, where 0 equal A and 25 equal Z.
    :param letter: int
    :return: the char equivalent value.
    """
    if isinstance(letter, str) is not False:
        return ord(letter) - ord('A')

class Task5:
    # Declare all the object we need.
    group_offset = ''
    encrypted_massage_key = ''
    massage_key = ''
    only_message = ''
    plug_board = {'Z': 'U', 'H': 'L', 'C': 'Q', 'W': 'M', 'O': 'A', 'P': 'Y', 'E': 'B', 'T': 'R', 'D': 'N', 'V': 'I'}

    rotorA = None
    rotorB = None
    rotorC = None

    plugboard = Plugboard(plug_board)

    def __init__(self): pass

    def get_message(self, message=None):
        """
        Get message.
        :param message: string.
        :return: the message.
        """
        if message is None:
            message = raw_input("Enter massage: ")

        for letter in message:
            if letter.isalpha() is not True:
                message = message.replace(letter, "")
            elif letter.islower():
                message = message.replace(letter, letter.upper())
        return message


    def extract_data(self, message):
        """
        Isolate only the relevant parts from the message.
        :param message: string.
        :return: decrypt / encrypt message.
        """
        message = ''.join(message)

        self.group_offset = message[:3]
        self.encrypted_massage_key = message[3:6]
        self.only_message = message[11:]

    def get_massage_key(self):
        """
        Get the offset by decrypt the mesage.
        :return: decrypted offset.
        """
        self.rotorA = Rotor(string_to_dict(rotors[3]), 4, letter_to_index(self.group_offset[2]), letter_to_index('X'))
        self.rotorB = Rotor(string_to_dict(rotors[4]), 5, letter_to_index(self.group_offset[1]), letter_to_index('I'))
        self.rotorC = Rotor(string_to_dict(rotors[1]), 2, letter_to_index(self.group_offset[0]), letter_to_index('S'))


        _enigma = Enigma(self.rotorA, self.rotorB, self.rotorC, self.plugboard)

        # The real offset.
        self.massage_key = _enigma.decrypt(message=self.encrypted_massage_key)

    def decrypt_message(self):
        """
        Decrypt the message itself.
        :return: decrypted message.
        """

        self.rotorA = Rotor(string_to_dict(rotors[3]), 4, letter_to_index(self.massage_key[2]), letter_to_index('X'))
        self.rotorB = Rotor(string_to_dict(rotors[4]), 5, letter_to_index(self.massage_key[1]), letter_to_index('I'))
        self.rotorC = Rotor(string_to_dict(rotors[1]), 2, letter_to_index(self.massage_key[0]), letter_to_index('S'))


        enigma = Enigma(self.rotorA, self.rotorB, self.rotorC, self.plugboard)

        # The decrypted message.
        return enigma.decrypt(message=self.only_message, show=True)

    def run(self, message):
        """
        Run the task.
        :param message: string.
        :return: the decrypted message.
        """
        self.extract_data(self.get_message(message))
        self.get_massage_key()
        self.decrypt_message()
