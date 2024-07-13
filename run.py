import argparse
import yaml

from tests_generator import TestsGenerator

parser = argparse.ArgumentParser()
parser.add_argument("input_yaml", help="The path and name of the input options file, refer to the readme.")
args = parser.parse_args()

with open(args.input_yaml, 'r') as file:
    user_input = yaml.safe_load(file)

generator = TestsGenerator(user_input)
generator.create_csv()
