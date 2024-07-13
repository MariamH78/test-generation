from datetime import datetime
import csv
import warnings

from validate_input import validate_input


class TestsGenerator:
    """
    A class to generate test cases based on user input options.

    Attributes:
        options (list): A list of options provided by the user.
        number_of_options (int): The number of options.
        generated_tests (list): A list to store generated test cases, with
                                each entry being a list that corresponds to the
                                values of the following fields:
                                    1- Master configuration for X (TRUE/FALSE/NA)
                                    2- Slave option for X (TRUE/FALSE/NA)
                                    3- Valid testcase (Yes/No)
                                    4- Expected value for X (TRUE/FALSE/NA)
                                with X being every user input option, and each X has its own column.
    """

    def __init__(self, user_input):
        """
        Initializes the TestsGenerator with user input and generates test cases.

        Args:
            user_input (dict): A dictionary containing user input.

        Raises:
            Warning: If the number of options is greater than 7, a warning is issued.
        """

        # Validate the input first,
        validate_input(user_input)

        # then initiailze the class members and generate the tests.
        self.options = user_input['options']
        self.options = [str(option) for option in self.options]

        self.number_of_options = len(user_input['options'])
        self.generated_tests = []

        # Warn user that the number of resulting combinations would be too high
        if (self.number_of_options > 7):
            warnings.warn("Given number of options is above 7, "
                        + "the program might take too long to run, "
                        + "and will use a lot of memory.")
            print("Press any key to proceed, or to cancel, press CTRL+C...")
            input()

        # If user chooses to proceed, the generator generates the tests.
        self._generate()

    def _generate(self):
        def generate_combinations(current_combination = [], counter = 0):
            """ Helper function that recursively generates combinations of options. """
            if counter >= 2 * self.number_of_options:
                self.generated_tests.append(current_combination.copy())
                return

            for setting in ['TRUE', 'FALSE', 'NA']:
                current_combination.append(setting)
                generate_combinations(current_combination, counter + 1)
                current_combination.pop()
            return

        def is_invalid(row_data):
            """
            Helper function that checks if a generated test case is invalid
            based on rules from the readme, returns True if invalid.
            """

            for i in range(self.number_of_options):
                if row_data[i] == 'FALSE' and                          \
                   row_data[i + self.number_of_options] == 'TRUE':
                    return True
                if (row_data[i] == 'TRUE' or row_data[i] == 'NA') and  \
                    row_data[i + self.number_of_options] == 'FALSE':
                    return True
            return False

        # In case the function is called multiple times,
        # this line makes sure the initial list is cleared first.
        self.generated_tests = []
        generate_combinations()

        for row in self.generated_tests:
            if (is_invalid(row)):
                row.append('NO')
                row += ['NA'] * self.number_of_options
            else:
                row.append('YES')
                expected_values = [row[i] if row[i] == 'FALSE' else 'TRUE' for i in range(self.number_of_options)]
                row += expected_values


    def create_csv(self):
        """
        Creates a CSV file with headers, all generated test cases, as well as their expected results.
        """

        header_row = ["Test case ID"]                                           \
                   + ["Master option for " + option for option in self.options] \
                   + ["Client option for " + option for option in self.options] \
                   + ["Valid TC"]                                               \
                   + ["Expected " + option for option in self.options]

        new_file_name = datetime.now().strftime('generated_tests_%y%m%d_%H%M%S.csv')
        with open(new_file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header_row)
            writer.writerows([i] + row for i, row in enumerate(self.generated_tests, 1))

        print(f"The file {new_file_name} was created successfully.")
