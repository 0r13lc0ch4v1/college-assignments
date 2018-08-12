from Reflector import Reflector
from Rotor import Rotor
from Substitutor import Substitutor
from Plugboard import Plugboard

# Rotors
rotors = ["EKMFLGDQVZNTOWYHXUSPAIBRCJ", "AJDKSIRUXBLHWTMCQGZNPYFVOE", "BDFHJLCPRTXVZNYEIWGAKMUSQO",
          "ESOVPZJAYQUIRHXLNFTGKDCMWB", "VZBRGITYUPSDNHLXAWMJQOFECK"]
# Reflector
R = "YRUHQSLDPXNGOKMIEBFZCWVJAT"


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


class Enigma(Substitutor):

    @property
    def offset(self):
        pass

    @property
    def letters_dict(self):
        pass
    """
    All the objects used in enigma.
    """
    plugboard = None

    rotorA = None
    rotorB = None
    rotorC = None
    reflector = Reflector(string_to_dict(R))

    counter = 0


    def __init__(self, _rotorA=None, _rotorB=None, _rotorC=None, _Plugboard=None):
        """
        Initialize the enigma.
        :param _rotorA: Rotor object.
        :param _rotorB: Rotor object.
        :param _rotorC: Rotor object.
        :param _Plugboard: Plugboard object.
        """

        super(Enigma, self)
        # check if the rotors not None - for constructor selection.
        if _rotorA is not None:
            self.rotorA = _rotorA
            self.rotorB = _rotorB
            self.rotorC = _rotorC

            self.plugboard = _Plugboard

        else:
            # If the arguments are None.
            self.initial_enigma()

    def is_value_Exist(self, val, _dictionary):
        """
        Check if the value exist in the dictionary.
        :param val: A-Z letter.
        :param _dictionary: dictionary.
        :return: boolean.
        """
        for key in _dictionary:
            if _dictionary[key] == val:
                return True
        return False

    def legal_input(self, key, action):
        """
        Check if the input is legal.
        :param key: int.
        :param action: string "rotor" or "offset".
        :return:
        """
        if action == "rotor":
            r = range(1, 6)
        if action == "offset":
            r = range(0, 26)

        if isinstance(key, int) is True:
            if key in r:
                return True
        else:
            return False

    # list of the rotors we used.
    global rotors_used
    rotors_used = {1: False, 2: False, 3: False, 4: False, 5: False}

    def Initial_rotor(self):
        """
        Initial rotor object for the enigma.
        :return: Rotor object.
        """
        error = "Illegal input! please follow instructions."
        global rotors_used
        # While the user try to input wrong values.
        while True:
            while True:
                try:
                    rotor_num = input("Enter rotor [1 to 5]: ")
                except NameError:
                    print error
                    continue
                except SyntaxError:
                    print error
                    continue
                if self.legal_input(rotor_num, "rotor") is not True:
                    print error
                    continue
                if rotors_used[rotor_num]:
                    print "You have already used this rotor, please choose another one."
                    continue
                rotors_used[rotor_num] = True
                break
            # Enter ring offset to the rotor.
            while True:
                ring_offset = raw_input("Enter ring offset of the rotor [A - Z]: ")
                if ring_offset.isalpha():
                    if len(ring_offset) == 1:
                        if ring_offset.islower():
                            ring_offset = ring_offset.upper()
                        ring_offset = self.letter_to_index(ring_offset)
                    else:
                        print error
                        continue
                else:
                    print error
                    continue
                break

            # Enter ring setting to the rotor.
            while True:
                ring_setting = raw_input("Enter ring setting of the rotor [A - Z]: ")
                if ring_setting.isalpha():
                    if len(ring_setting) == 1:
                        if ring_setting.islower():
                            ring_setting = ring_setting.upper()
                        ring_setting = self.letter_to_index(ring_setting)
                else:
                    print error
                    continue
                break

            return Rotor(string_to_dict(rotors[rotor_num - 1]), rotor_num, ring_offset, ring_setting)

    def Initial_plugboard(self):
        """
        Initial Plugboard object.
        :return: Plugboard object.
        """
        _plugboard = dict()
        error = "Illegal input! please follow instructions\n" \
                "[non alphabetic characters will stop the connecting process].\n"

        stop = False
        while stop is not True:
            while True:
                print "Please enter two letters you want to connect [non alpha to stop]."
                letter_one = raw_input("The first letter: ")
                if letter_one.isalpha() is not True:
                    stop = True
                    break
                letter_two = raw_input("The second letter: ")
                if letter_two.isalpha() is not True:
                    stop = True
                    break
                print
                if len(letter_one) == 1 and len(letter_two) == 1:
                    if letter_one.islower():
                        letter_one = letter_one.upper()
                    if letter_two.islower():
                        letter_two = letter_two.upper()
                    if letter_one in _plugboard or letter_two in _plugboard or self.is_value_Exist(letter_one, _plugboard) or self.is_value_Exist(letter_two, _plugboard):
                        print "Letters already connected. Please try again [non alpha to stop]"
                    else:
                        _plugboard[letter_one] = letter_two
                else:
                    print "Please enter one letter at a time."

        self.plugboard = Plugboard(_plugboard)

    def circular_shifts(self):
        pass

    def forward_translation(self, letter):
        """
        Go through all of the rotors in forward direction.
        :param letter: A-Z char.
        :return: the forward value.
        """
        return self.reflector.forward_translation(
            self.rotorC.forward_translation(self.rotorB.forward_translation(self.rotorA.forward_translation(letter))))

    def reverse_translation(self, letter):
        """
        Go through all of the rotors in reverse direction.
        :param letter: A-Z char.
        :return: the reverse value.
        """
        return self.rotorA.reverse_translation(self.rotorB.reverse_translation(self.rotorC.reverse_translation(letter)))

    def get_input(self):
        """
        Get the plain text from the user.
        :return: return a string ot only A-Z characters.
        """
        plain_text = raw_input(
            'Please enter plain text [non alphabetic characters will be discarded]:\n')
        for letter in plain_text:
            if letter.isalpha() is not True:
                plain_text = plain_text.replace(letter, "")
            elif letter.islower():
                plain_text = plain_text.replace(letter, letter.upper())
        return plain_text

    # Manually create the enigma.
    def initial_enigma(self):
        """
        Initialize the enigma machine.
        :return: the ciphered text.
        """

        # Initialize all three rotors.
        self.rotorA = self.Initial_rotor()
        self.rotorB = self.Initial_rotor()
        self.rotorC = self.Initial_rotor()

        # Give the user an option if to set a plugboard.
        ans = raw_input("Do you want to initialize plugboard? [y or n]")
        if ans == 'y' or ans == 'Y':
            self.Initial_plugboard()
        else:
            self.plugboard = Plugboard(dict())

    def decrypt(self, message=None, show=False):
        """
        decrypt/encrypt a text (same thing).
        :param message: string.
        :param show: show prints or not.
        :return: the encrypted / decrypted text.
        """
        # Print the rotors information.
        if show:
            print "\nSTART MACHINE STATE:"
            print "Right rotor: offset - " + self.index_to_letter(self.rotorA.offset) + ".   ring offset - " + self.index_to_letter(
                self.rotorA.ring_setting) + "."
            print "Middle rotor: offset - " + self.index_to_letter(self.rotorB.offset) + ".   ring offset - " + self.index_to_letter(
                self.rotorB.ring_setting) + "."
            print "Left rotor: offset - " + self.index_to_letter(self.rotorC.offset) + ".   ring offset - " + self.index_to_letter(
                self.rotorC.ring_setting) + ".\n"

            print "Your plugboard is: "
            print self.plugboard.letters_dict
            print

        counter = 0
        plain_text = ""
        cipher_text = ""

        if message is None:
            message = self.get_input()

        # Check the turnover state.
        for letter in message:
            plain_text += letter
            if self.rotorA.is_turnover_notch() or self.rotorB.is_turnover_notch():
                if self.rotorB.is_turnover_notch():
                    self.rotorC.circular_shifts()
                self.rotorB.circular_shifts()
            self.rotorA.circular_shifts()

            letter = self.plugboard.get_letter(letter)
            cipher_text += self.plugboard.get_letter(self.reverse_translation(self.forward_translation(letter)))

            counter = (counter + 1) % 5
            if counter == 0:
                cipher_text += ' '
                plain_text += ' '

        if show:

            # Print the plain and the cipher text.
            print "The plain text:\n" + plain_text
            print "The cipher text:\n" + cipher_text

            # Print the rotors information.
            print "\nFINAL MACHINE STATE:"
            print "Right rotor: offset - " + self.index_to_letter(self.rotorA.offset) + ".   ring offset - " + self.index_to_letter(
                self.rotorA.ring_setting) + "."
            print "Middle rotor: offset - " + self.index_to_letter(self.rotorB.offset) + ".   ring offset - " + self.index_to_letter(
                self.rotorB.ring_setting) + "."
            print "Left rotor: offset - " + self.index_to_letter(self.rotorC.offset) + ".   ring offset - " + self.index_to_letter(
                self.rotorC.ring_setting) + ".\n"

        # Return the text after the machine.
        return cipher_text