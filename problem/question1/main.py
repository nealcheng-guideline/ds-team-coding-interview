"""
Prompt: You have joined a new team and are working on migrating a legacy codebase to a new platform.
You found the following function. Take a few minutes to read the code.

The Decimal class in Python's standard library offers exact decimal arithmetic, which makes it a perfect fit 
for domains like finance, accounting or anywhere you can't afford those pesky binary floating rounding errors.
It can be used like a number Decimal(1.22) + Decimal(0.79)
"""


from decimal import Decimal
import logging

def to_decimal(in_dollars):
    try:
        in_dollars = float(in_dollars)
        in_dollars = Decimal(in_dollars)
        return in_dollars
    except ValueError:  # cases when input string cannot be coerced into a float
        if not in_dollars:  # cases when input string is an empty string
            return 0
        raise ValueError(f"Unable to parse field with value {in_dollars} as float")
    except TypeError:
        if in_dollars is None:  # cases when input string is None
            logger = logging.getLogger(__name__)
            logger.debug("Trying to convert None to float - defaulting to 0")
            return 0
        raise ValueError(f"Unable to parse field with value {in_dollars} as float")


"""
Q1.1: What does this function do? Describe in 1-2 sentences.
"""

"""
Q1.2: What will be the outputs of the following? Based on the code, infer the value and type of the output.

to_decimal("100")
to_decimal("")
to_decimal("one")
to_decimal(None)
to_decimal(0.0)
"""

"""
Q1.3: Given that this is a production code, what are the potential issues with the code? 
"""

"""
Q1.4: Rewrite the function to be more robust given the issues that you've identified & explain your changes.
You can modify and run the main function below to test the provided examples and verify that your function behaves as expected.
"""

"""
[Extra Credit] Q1.5: You are then told to add a functionality to convert dollars to cents in the same function. 
Do you think this is a good idea?
"""

if __name__ == "__main__":
    for _input in (None, "", "0", 0, 0.0):
        answer = to_decimal(_input)
        if answer != Decimal(0):
            raise AssertionError(f"Error: {_input} should be converted to {Decimal(0)}")
        if not isinstance(answer, Decimal):
            raise AssertionError(f"Error: {_input} should be converted to {Decimal(0)}")