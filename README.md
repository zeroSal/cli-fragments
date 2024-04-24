# cli-fragments
[![Pylint](https://github.com/zeroSal/cli-fragments/actions/workflows/pylint.yml/badge.svg)](https://github.com/zeroSal/cli-fragments/actions/workflows/pylint.yml)

Awesome terminal input and output functions for python scripts.

![jigsaw](https://github.com/zeroSal/cli-fragments/assets/38191926/6f22384b-ca65-49cd-bb00-2f1767739f95)

[Icon by by Pop Vectors - Flaticon](https://www.flaticon.com/free-icons/puzzle")

## Why this name?
I like to consider the command-line interface as if it were a graphical interface. In the development of graphical interfaces, 'components' are usually used to facilitate maintainability and design consistency. In my opinion, the word 'fragments' is a correct synonym to describe the same approach, but for command-line interfaces.

## Fragments
 - `error`: a red message having `[✕]` as prefix
 - `success`: a green message having `[✓]` as prefix
 - `warning`: a yellow message having `[!]` as prefix
 - `text`: a standard text in terminal having the proper padding
 - `debug`: a default color message having `[#]` as prefix
 - `notice`: a blue message having `[~]` as prefix
 - `ask`: a qustion to the user having `[?]` as prefix. The input value can be optionally validated passing a `validator` callback

## Screenshot
![image](https://github.com/zeroSal/cli-fragments/assets/38191926/1cb3b75d-bc35-4ef4-bd09-f99c5d79a31c)


## Usage

First of all, you have to install the library using `pip`.
```shell
pip install cli-fragments
```

Then import the library in your script and use it as follows.
```python
from cli_fragments import CliFragments

# Custom validators function.
# They must accept an str parameter and must raise ValueError on validation failure.
def validator_function(value: str):
    if value == "wrong":
        raise ValueError

# Instantiate the main class
io = CliFragments()

# Use the output methods as shown
io.debug("This is a debug message.")
io.notice("This is a notice message.")
io.warning("This is a warning message.")
io.error("This is an error message.")
io.success("This is a success message.")
io.text("This is padded raw text message.")

# The default and the validator parameters are optional in the ask method.
# You can pass None to avoid using them.
io.ask("This is a user question.", None, None)

# This is a validated ask method call having a default value.
io.ask("This is a user question.", "default", validator_function)
```
