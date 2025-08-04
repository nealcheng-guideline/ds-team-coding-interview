"""
## Purpose
This exercise will test the candidate's ability to read buggy legacy code and refactor into something more
maintainable.  The final code should be robust, able to handle varying types and coercing it into a fixed type.  


## Factors for consideration:
Readability
Correctness
Type handling/hinting
Exception handling
Simplicity
Proper Variable naming


## Potential questions:
What do I do about these exceptions?  | Up to the candidate.  Either execute "look before you leap", or "easier to ask for forgiveness"
I'm not familiar with the Decimal class.  How can I handle the exceptions? |. You can perform an intermediate coercion into the right data structure which you are confident about putting into Decimal

## Issues:

Inconsistent type returns:  Need to choose a correct type.  
Inconsistent logging: pull out get_logger to top of file
Unused ValueErrors
Two separate functions within one try clause
Maintaining same return

Can he/she account for all exceptions?
1. None
2. Empty string
3. Non-numeric string


## Extra credit:
Better naming
Joint return at the end
Logger not of the right level.  This is supposed to be logger.error
Writing proper assertions
"""



from typing import Optional
import logging
from decimal import Decimal

logger = logging.getLogger(__name__)

def to_decimal_solution(dollars: Optional[int | float | str]) -> Decimal:

    if not dollars: # account for zero ints/floats, empty strings.  
        logger.warning(f"in_dollars is of type {type(dollars)} and equal to {dollars}.  Returning a Decimal(0.0)")
        return Decimal(0)
    
    # this is an extra credit, given that the argument can be string
    if isinstance(dollars, str):
        if not dollars.isnumeric():
            raise ValueError(f"dollars is of type string and not numeric")
        else:
            dollars = float(dollars)
    #################################################################################################

    return Decimal(dollars)

"""
Answer to the follow-up question: 
You are then told to add a functionality to return cents. Is this a good idea?  How would you incorporate this proposal?

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Adding cents would increase the number of return types, which would unfortunately increase the amount of downstream handling
A separate function should be used, given the simplicity of this code logic.  
if a candidate gets this wrong, it's not a dealbreaker, but it shows that his/her design is suboptimal.  

The second best solution is if he/she decides to incorporate this as an argument, the solution is to multiply the in_dollars by 100.  Ensure that the candidate
will now return as an int.  
"""

if __name__ == "__main__":
    for _input in (None, "0", 0, 0.0):
        answer = to_decimal_solution(_input)
        assert answer == Decimal(0)
        assert isinstance(answer, Decimal)