from datetime import datetime
import csv
import warnings

class TestsGenerator:
    def __init__(self, input):
        self.options = input['options']
        self.number_of_options = len(input['options'])
        self.generated_tests = []
        if (self.number_of_options >= 8):
            warnings.warn("Given number of options is above 7, the program might take too long to run.")
        self._generate()

    def _generate(self):
        def generate_combinations(current_combination = [], counter = 0):
            if counter >= 2 * self.number_of_options:
                self.generated_tests.append(current_combination.copy())
                return

            for setting in ['TRUE', 'FALSE', 'NA']:
                current_combination.append(setting)
                generate_combinations(current_combination, counter + 1)
                current_combination.pop()
            return
        def is_invalid(row_data):
            for i in range(self.number_of_options):
                if row_data[i] == 'FALSE' and                          \
                   row_data[i + self.number_of_options] == 'TRUE':
                    return True

                if (row_data[i] == 'TRUE' or row_data[i] == 'NA') and  \
                    row_data[i + self.number_of_options] == 'FALSE':
                    return True

            return False

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
        header_row = ["Test case ID"]                                           + \
                     ["Master option for " + option for option in self.options] + \
                     ["Client option for " + option for option in self.options] + \
                     ["Valid TC"]                                               + \
                     ["Expected " + option for option in self.options]

        new_file_name = datetime.now().strftime('generated_tests_%y%m%d_%H%M%S.csv')
        with open(new_file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header_row)
            writer.writerows([i] + row for i, row in enumerate(self.generated_tests, 1))

        print(f"The file {new_file_name} was created successfully.")
