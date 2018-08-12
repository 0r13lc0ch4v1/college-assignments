from abc import ABCMeta
from Substitutor import Substitutor

# Abstract class.
class Translator(Substitutor):
    __metaclass__ = ABCMeta

    @property
    def offset(self):
        """
        Offset property.
        :return: offset object.
        """
        return

    @offset.setter
    def offset(self, new_offset):
        """
        Offset property setter.
        :return: revalue offset object.
        """
        self.offset = new_offset

    @property
    def letters_dict(self):
        """
        Dictionary property.
        :return: dictionary object.
        """
        return

    def __init__(self):
        super(Translator, self)

    def is_dictionary_legal(self, dictionary):
        """
        Check if the dictionary stand with the class standard.
        :param dictionary: the class property.
        :return: boolean.
        """

        def has_duplicate_values(_dictionary):
            """
            Dictionary value can't duplicate.
            :param _dictionary: the class property.
            :return: boolean.
            """
            for key_a in _dictionary:
                for key_b in _dictionary:
                    if key_a != key_b:
                        if _dictionary[key_a] == _dictionary[key_b]:
                            return False
            return True

        def are_legal_elements(_dictionary):
            """
            Dictionary values are legal.
            :param _dictionary: the class property.
            :return: boolean.
            """
            for key in _dictionary:
                if isinstance(key, int) is not True or isinstance(_dictionary[key], str) is not True:
                    return False
                if _dictionary[key].isupper() is not True:
                    return False
            return True

        if isinstance(dictionary, dict) is not True:
            return False

        if len(dictionary) > 26:
            return False

        if are_legal_elements(dictionary) is not True:
            return False

        if has_duplicate_values(dictionary) is not True:
            return False

        return True

    def is_legal_input(self, _input):
        """
        Check if input is legal - must be A-Z character.
        :param _input: the class property.
        :return: boolean.
        """
        if isinstance(_input, str) is not True:
            return False

        if _input.isupper() is not True:
            return False

        return True

    def circular_shifts(self):
        """
        Increment the offset.
        """
        self.offset = (self.offset + 1) % 26

    def forward_translation(self, letter):
        """
        Create the forward value of the rotor.
        :param letter: A-Z char
        :return: the forward rotor output.
        """
        if self.is_legal_input(letter) is not True:
            return False

        else:
            index = self.letter_to_index(letter)
            index = (index + self.offset - self.ring_setting) % 26
            index = self.letter_to_index(self.letters_dict[index])
            index = (index - self.offset + self.ring_setting) % 26
            return self.index_to_letter(index)

    def reverse_translation(self, letter):
        """
        Create the reverse value of the rotor.
        :param letter: A-Z char
        :return: the reverse rotor output.
        """
        if self.is_legal_input(letter) is not True:
            return False

        else:
            index = self.letter_to_index(letter)
            index = (index + self.offset - self.ring_setting) % 26
            index = self.get_key_by_value(self.index_to_letter(index), self.letters_dict)
            index = (index - self.offset + self.ring_setting) % 26
            return self.index_to_letter(index)
