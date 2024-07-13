import argparse
import yaml

from validate_input import validate_input
from tests_generator import TestsGenerator

parser = argparse.ArgumentParser()
parser.add_argument("input_yaml", help="The path and name of the input options file, refer to the readme.")
args = parser.parse_args()

with open(args.input_yaml, 'r') as file:
    user_input = yaml.safe_load(file)

# Validate the input first,
validate_input(user_input)

# then generate the tests.
generator = TestsGenerator(user_input)
generator.create_csv()
