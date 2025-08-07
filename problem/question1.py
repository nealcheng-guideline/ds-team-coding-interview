"""
Prompt: You have joined a new team and are working on migrating a legacy codebase to a new platform.
You found the following function. Take a few minutes to read the code.


The Decimal class in Python's standard library offers exact decimal arithmetic, which makes it a perfect fit 
for domains like finance, accounting or anywhere you can't afford those pesky binary'floating rounding errors.
It can be used like a number Decimal(1.22) + Decimal(0.79)

"""


from decimal import Decimal
import logging

def to_decimal(in_dollars):
    try:
        in_dollars = float(in_dollars)
        in_dollars = Decimal(in_dollars)
        return in_dollars
    except ValueError:
        if not in_dollars:
            return 0
        raise ValueError(f"Unable to parse field with value {in_dollars} as float")
    except TypeError:
        if in_dollars is None:
            logger = logging.getLogger(__name__)
            logger.debug("Trying to convert None to float - defaulting to 0")
            return 0
        raise ValueError(f"Unable to parse field with value {in_dollars} as float")


"""
Q1: What does this function do? Describe in 1-2 sentences.
"""

"""
Q2: What will be the outputs of the following? Based on the code, infer the value and type of the output.

to_decimal("100")
to_decimal("")
to_decimal("one")
to_decimal(None)
to_decimal(0.0)
"""

"""
Q3: Given that this is a production code, what are the potential issues with the code? 
Consider type safety, error handling, and maintainability.
"""

"""
Q4: Rewrite the function to be more robust given the issues that you've identified & explain your changes.
Let's run the script to see if the function is robust.
"""

"""
Q5: You are then told to add a functionality to convert dollars to cents in the same function. 
Discuss both pros and cons of this proposal and outline a possible implementation.
(Candidate only need to discuss whether this is a good solution and how to implement it)
"""

if __name__ == "__main__":
    for _input in (None, "0", 0, 0.0):
        answer = to_decimal(_input)
        if answer != Decimal(0):
            raise AssertionError(f"Error: {_input} should be converted to {Decimal(0)}")
        if not isinstance(answer, Decimal):
            raise AssertionError(f"Error: {_input} should be converted to {Decimal(0)}")