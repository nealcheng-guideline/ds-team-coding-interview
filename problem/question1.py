"""
Prompt: You have joined a new team and are working on migrating a legacy codebase to a new platform.
You found the following function. Take a few minutes to read the code.
"""


from decimal import Decimal
import logging

logger = logging.getLogger(__name__)

def to_decimal(in_dollars):
    try:
        in_dollars = float(in_dollars)
        in_dollars = Decimal(in_dollars)
        return in_dollars
    except ValueError:  # cases when input string cannot be coerced into a float
        # handles cases when input string is ''
        if not in_dollars:
            return 0
        raise ValueError(f"Unable to parse field with value {in_dollars} as float")
    except TypeError:  # cases when input string is None
        if in_dollars is None:  # we'll default to 0
            logger.debug("Trying to convert None to float - defaulting to 0")
            return 0
        raise ValueError(f"Unable to parse field with value {in_dollars} as float")


"""
Q1: What does this function do? Describe in 1-2 sentences.
"""

"""
Q2: What will be the outputs of the following?

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
