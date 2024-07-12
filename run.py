import argparse
import yaml

from input_validator import InputValidator
from tests_generator import TestsGenerator

parser = argparse.ArgumentParser()
parser.add_argument("input_yaml", help="The path and name of the input options file, refer to the readme.")
args = parser.parse_args()

with open(args.input_yaml, 'r') as file:
    input = yaml.safe_load(file)

# Validate the input first,
InputValidator(input)

# then generate the tests.
generator = TestsGenerator(input)
generator.create_csv()
