from Translator import Translator

turnover_notch = {1: 'Q', 2: 'E', 3: 'V', 4: 'J', 5: 'Z'}


class Rotor(Translator):
    rotor_num = 0

    @property
    def offset(self):
        """
        The rotor offset.
        :return: The rotor offset
        """
        return self._offset

    @offset.getter
    def offset(self):
        """
        Getter of the rotor offset
        :return: rotor offset
        """
        return self._offset

    @offset.setter
    def offset(self, new_offset):
        """
        Set the rotor offset.
        """
        self._offset = new_offset

    @property
    def ring_setting(self):
        """
        The rotor ring setting..
        :return: The rotor ring setting.
        """
        return self._ring_setting

    @ring_setting.getter
    def ring_setting(self):
        """
        Get the rotor ring setting..
        :return: The rotor ring setting.
        """
        return self._ring_setting

    @ring_setting.setter
    def ring_setting(self, new_ring_setting):
        """
        Set the rotor ring setting.
        """
        self._ring_setting = new_ring_setting

    @property
    def letters_dict(self):
        """
        The rotor dictionary.
        :return: the rotor dictionary
        """
        return self._letters_dict

    @letters_dict.setter
    def letters_dict(self, new_dict):
        """
        Set the rotor dictionary.
        """
        self._letters_dict = new_dict

    @letters_dict.getter
    def letters_dict(self):
        """
        Get rotor dictionary.
        :return: the rotor dictionary
        """
        return self._letters_dict

    def is_turnover_notch(self):
        """
        Check if the rotor is in turnover position.
        :return: boolean.
        """
        if self.offset == self.letter_to_index(turnover_notch[self.rotor_num]):
            return True
        else:
            return False

    def __init__(self, rotor, _rotor_num, new_offset, _ring_setting):
        """
        Initialize rotor object.
        :param rotor: Rotor object.
        :param _rotor_num: int.
        :param new_offset: int.
        :param _ring_setting: int.
        """
        super(Rotor, self)
        if self.is_dictionary_legal(rotor) is True:
            self.letters_dict = rotor
            self.rotor_num = _rotor_num
        else:
            self.letters_dict = dict()

        if isinstance(new_offset, int) is True:
            self._offset = new_offset
        else:
            self._offset = 0

        if isinstance(_ring_setting, int) is True:
            self._ring_setting = _ring_setting
        else:
            self._ring_setting = 0


