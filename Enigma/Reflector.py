from Translator import Translator


class Reflector(Translator):

    @property
    def letters_dict(self):
        """
        The rotor dictionary.
        :return: the rotor dictionary.
        """
        return self._letters_dict

    def __init__(self, reflector):
        super(Reflector, self)
        if self.is_dictionary_legal(reflector) is True:
            self._letters_dict = reflector
        else:
            self._letters_dict = dict()

    # Doesn't have offset to shift.
    def circular_shifts(self): pass

    def forward_translation(self, letter):
        """
        The reflector forward.
        :param letter: A-Z char.
        :return: reflector forward output.
        """
        if self.is_legal_input(letter) is not True:
            return False

        else:
            index = self.letter_to_index(letter)
            return self._letters_dict[index]

    # Doesn't have revers translation.
    def reverse_translation(self, letter): pass