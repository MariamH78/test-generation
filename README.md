
# test-generation:
A tests generator for a hypothetical server scenario, where the server can connect to two clients:
- First client connected to the server becomes a master client that is able to configure the server with any number of boolean global options.
- Second client to connect is a slave and is not able to reconfigure these  options with different values, an error state will be reached.
- If the slave client configures the server with same values already set by the master client, no errors occur.
- If master client didn’t configure some of the parameters of the server, they run with the default value: `True`.

The program takes in a YAML file with the required boolean options as an input, and the `TestsGenerator` object generates all possible combinations of configurations for both master and client (`TRUE`, `FALSE`, `NA` (Default  value, or not applicable)).

The user can optionally call `create_csv()`, which creates a .csv file with the generated test cases in the following format (for example, this is a part of the generated output for the `sample_input.yaml`:
Test case ID |Master option for buffer_data | Master option for enable_timeout | Client option for buffer_data | Client option for enable_timeout | Valid TC | Expected buffer_data | Expected enable_timeout
--- | --- | --- | --- | --- | --- | --- | --- 
1|TRUE|TRUE|TRUE|TRUE|YES|TRUE|TRUE
2|TRUE|TRUE|TRUE|FALSE|NO|NA|NA
3|TRUE|TRUE|TRUE|NA|YES|TRUE|TRUE 
..|..|..|..|..|..|..|.. 
79|NA|NA|NA|TRUE|YES|TRUE|TRUE
80|NA|NA|NA|FALSE|NO|NA|NA
81|NA|NA|NA|NA|YES|TRUE|TRUE

## To run locally:
1. Clone the repository

```sh
git clone https://github.com/MariamH78/test-generation.git 
```
2. Install the dependencies (and optionally, create a virtual environment using `venv`)
```sh
python -m pip install -r requirements.txt
```

3. To run, call `run.py` and pass in an argument with the YAML file input, preceded with the full absolute/relative path if the file is not in the same directory.
```sh
run.py path/to/dir/input.yaml
```
To run the sample file:
```sh
run.py sample_input.yaml
```
## More on the input YAML file:
The input file must include the key `options` and it must be followed by a list of the required options. Regardless of the datatypes of the items on the list, each item will be handled as a string in the final table. Quotation marks are optional.

Input is validated based on a few rules, if any of them is broken, an exception will be raised, and the program will terminate.

1. The input YAML file cannot be empty, this raises `NoOptionsKeyError`.
2.	The input YAML file must have the key ‘options’, violating this raises `NoOptionsKeyError`.
3.	The key ‘options’ must have a non-empty list of values, violating this raises `EmptyOptionsError`.
4.	The non-empty list of values can’t have any repeated values, violating this raises `RepeatedOptionsError`.
5.	Each value cannot have any special characters or non-ASCII characters, violating this raises `SpecialCharactersError`. Special characters are defined as any character from the following:

! | | “ |# | $ | % | & | ‘ | ( | ) | \| | * | + | , | - | . | / | : | ; | < | = | > | ? | @ | [ | ] | \ | ^ | ` | { | } | ~
-- | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - 

