from Translator import Translator


class Plugboard(Translator):

    @property
    def letters_dict(self):
        """
        The rotor dictionary.
        :return: the rotor dictionary.
        """
        return self._letters_dict

    @letters_dict.getter
    def letters_dict(self):
        """
        Get The rotor dictionary.
        :return: the rotor dictionary.
        """
        return self._letters_dict

    def __init__(self, plugboard):
        """
        Initialize the plugboard object.
        :param plugboard:
        """
        super(Plugboard, self)
        if self.is_plugboard_legal(plugboard) is True:
            self._letters_dict = plugboard
        else:
            self._letters_dict = dict()

    def is_plugboard_legal(self, plugboard):
        """
        Check if the plugboard valid.
        :param plugboard: dictionary.
        :return: boolean.
        """
        def has_duplicate_values(_plugboard):
            """
            Check their are no duplicate.
            :param _plugboard: dictionary.
            :return: boolean.
            """
            for key_a in _plugboard:
                for key_b in _plugboard:
                    if key_a != key_b:
                        if _plugboard[key_a] == _plugboard[key_b]:
                            return False
            return True

        def is_all_uppercase(_plugboard):
            """
            check if all the letters are uppercase.
            :param _plugboard: dictionary.
            :return: boolean.
            """
            for key in _plugboard:
                if isinstance(key, str) is not True or isinstance(_plugboard[key], str) is not True:
                    return False
                if key.isupper() is not True or _plugboard[key].isupper() is not True:
                    return False
                return True

        if isinstance(plugboard, dict) is not True:
            return False

        if len(plugboard) > 20:
            return False

        if is_all_uppercase(plugboard) is not True:
            return False

        if has_duplicate_values(plugboard) is not True:
            return False

        return True

    # Doesn't have offset to shift.
    def circular_shifts(self): pass

    # Doesn't have forward translation.
    def forward_translation(self, key): pass

    # Doesn't have revers translation.
    def reverse_translation(self, value): pass

    def get_letter(self, letter):
        """
        The plugboard purpose, return the connected letter if exist.
        :param letter: A-Z char.
        :return: the connected letter if exist.
        """
        if letter in self.letters_dict:
            return self._letters_dict[letter]
        elif letter in self.letters_dict.values():
            return self.get_key_by_value(letter, self.letters_dict)
        else:
            return letter