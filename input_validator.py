from input_validation_exceptions import *

class InputValidator:
    def __init__(self, input):
        if not input or 'options' not in input:
            raise NoOptionsKeyError

        self.options = input['options']

        if not self.options:
            raise EmptyOptionsError
        if bad_options:= self.has_special_characters():
            raise SpecialCharactersError(bad_options)
        if duplicates := self.duplicated_options():
            raise RepeatedOptionsError(duplicates)

    def has_special_characters(self):
        special_characters = " !\"#$%&'()*+,-./:;<=>?@[\]^`{|}~"
        opts_with_special_chars = set()
        for option in self.options:
            if not option.isascii() or any(c in special_characters for c in option):
                opts_with_special_chars.add(option)

        return opts_with_special_chars

    def duplicated_options(self):
        checking_set = set()
        duplicates = set()
        for option in self.options:
            if option in checking_set:
                duplicates.add(option)
            else:
                checking_set.add(option)
        return duplicates
