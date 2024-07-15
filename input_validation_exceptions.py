class EmptyOptionsError(Exception):
    def __init__(self):
        self.message = "The provided input file has an empty list of options."
        super(EmptyOptionsError, self).__init__(self.message)
    
class BlankOptionError(Exception):
    def __init__(self):
        self.message = "The provided list of options has one or more blank options."
        super(BlankOptionError, self).__init__(self.message)

class SpecialCharactersError(Exception):
    def __init__(self, special_characters_options=None):
        self.message = "The following options have special characters: " \
                     + ", ".join([('"' + option + '"') for option in special_characters_options])
        super(SpecialCharactersError, self).__init__(self.message)

class RepeatedOptionsError(Exception):
    def __init__(self, duplicated_options=None):
        self.message = "The following options are repeated in the input file: " \
                     + ", ".join([('"' + option + '"') for option in duplicated_options])
        super(RepeatedOptionsError, self).__init__(self.message)

class NoOptionsKeyError(Exception):
    def __init__(self):
        self.message = "No 'options' key in the YAML file."
        super(NoOptionsKeyError, self).__init__(self.message)
