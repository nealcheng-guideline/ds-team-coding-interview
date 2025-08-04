"""
You have joined a new team.  During a migration you have found poorly written legacy code.
Given its widespread use, your goal is to design this function for robustness against all types of inputs.
Please assume you are working with production code, so please treat this exercise as if you're an employee. 

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
You are then told to add a functionality to return cents. Is this a good idea?  How would you incorporate this proposal?
(Candidate only need to discuss whether this is a good solution and how to implement)
"""


if __name__ == "__main__":
    pass
