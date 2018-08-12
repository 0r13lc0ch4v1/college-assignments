from abc import ABCMeta, abstractproperty, abstractmethod


# Abstract class
class Substitutor():
    __metaclass__ = ABCMeta

    @abstractproperty
    def offset(self):
        """
        Abstract property for the rotor offset.
        :return: the offset object.
        """
        return

    @offset.setter
    def offset(self, new_offset):
        """
        Abstract property for the rotor offset setter.
        :return: the offset setter object.
        """
        return

    @abstractproperty
    def letters_dict(self):
        """
        Abstract property for the rotor / reflector / plugboard dictionary.
        :return: the dictionary object.
        """
        return

    @letters_dict.setter
    def letters_dict(self, new_letters_dict):
        """
        Abstract property for the rotor / reflector / plugboard dictionary.
        :return: the dictionary setter object.
        """
        return

    def __init__(self): pass

    def letter_to_index(self, letter):
        """
        Translate letter to index, where A equal 0 and Z equal 25.
        :param letter: char
        :return: the index equivalent value.
        """
        if isinstance(letter, str) is not False:
            return ord(letter) - ord('A')

    def index_to_letter(self, index):
        """
        Translate index to char, where 0 equal A and 25 equal Z.
        :param letter: int
        :return: the char equivalent value.
        """
        index_range = range(0, 26)

        # Check if the index is in a valid range.
        if index in index_range:
            return chr(index + ord('A'))

    def get_key_by_value(self, val, _dictionary):
        """

        :param val: value of dictionary.
        :param _dictionary: dictionary object.
        :return: If value exist in dictionary, the key returned else return val.
        """
        for key in _dictionary:
            if _dictionary[key] == val:
                return key
        return val

    # Abstract function to implement in the derived classes.
    @abstractmethod
    def circular_shifts(self): pass

    # Abstract function to implement in the derived classes.
    @abstractmethod
    def forward_translation(self, letter): pass

    # Abstract function to implement in the derived classes.
    @abstractmethod
    def reverse_translation(self, letter): pass
