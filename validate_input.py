from input_validation_exceptions import *

def has_special_characters(options):
    """
    Checks for special characters in the given options. The reference for
    special characters' selection is [https://owasp.org/www-community/password-special-characters],
    with the exclusion of the underscore. Numbers are allowed.

    Args:
        options (list of strings): A list of options to check.

    Returns:
        set: A set of options that contain special characters.
    """

    special_characters = " !\"#$%&'()*+,-./:;<=>?@[\]^`{|}~"
    opts_with_special_chars = set()
    for option in options:
        if not option.isascii() or any(c in special_characters for c in option):
            opts_with_special_chars.add(option)
    return opts_with_special_chars

def duplicated_options(options):
    """
    Checks for duplicated options in the given options.

    Args:
        options (list of strings): A list of options to check.

    Returns:
        set: A set of duplicated options (can be empty).
    """

    checking_set = set()
    duplicates = set()
    for option in options:
        if option in checking_set:
            duplicates.add(option)
        else:
            checking_set.add(option)
    return duplicates

def validate_input(user_input):
    """
    Validates the user input and raises exceptions if anything is wrong.
    If input is correct, returns nothing.

    Args:
        user_input (dict): A dictionary containing user input, expected to have a key 'options'
                           with a list of option strings.

    Raises:
        NoOptionsKeyError: If the 'options' key is missing from user_input or if the file is empty.
        EmptyOptionsError: If the 'options' list is empty.
        SpecialCharactersError: If any option contains special characters.
        RepeatedOptionsError: If there are duplicated options in the 'options' list.
    """

    if not user_input or 'options' not in user_input:
        raise NoOptionsKeyError

    options = user_input['options']

    if not options:
        raise EmptyOptionsError
        
    options = [str(option) for option in options]


    if bad_options:= has_special_characters(options):
        raise SpecialCharactersError(bad_options)

    if duplicates := duplicated_options(options):
        raise RepeatedOptionsError(duplicates)
