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
Will there be any "salary_dollars" field with dollars signs within the string? |  No


## Q1: attempt to convert the given input (of any type) into a decimal object (although it returns 0 for certain edge cases)

## Q2: 
to_decimal("100")  -> Decimal('100')
to_decimal("")     -> 0
to_decimal("one")  -> ValueError
to_decimal(None)   -> 0
to_decimal(0.0)    -> Decimal('0')

## Q3: 
Inconsistent type returns:  Need to choose a correct type.  
Inconsistent logging: pull out get_logger to top of file
Unused ValueErrors
Two separate functions within one try clause
Maintaining same return


## Q4: see the sample code below
Required
- consistent return type (Decimal)
- consistent error handling & logging
- explicit handling of edge cases 


Extra credit:
- Better naming
- Joint return at the end
- Logger not of the right level.  This is supposed to be logger.error
- Writing proper assertions
- Option to allow the caller to specify a default value for invalid input (other than 0)

## Source
https://github.com/guideline-data/python-web-api/blob/master/src/new_comp/utils.py#L129-L147
"""



from typing import Optional
import logging
from decimal import Decimal

logger = logging.getLogger(__name__)

def to_decimal(dollars: Optional[int | float | str]) -> Decimal:

    if not dollars: # account for zero ints/floats, empty strings.  
        logger.warning(f"in_dollars is of type {type(dollars)} and is equal to {dollars}.  Returning a Decimal(0.0)")
        return Decimal(0)
    
    # this is an extra credit, given that the argument can be string
    # caveat here is that isnumeric does not recognize stringified floats (4000.0) as numeric.  
    if isinstance(dollars, str):
        if not dollars.isnumeric():
            # extra credit for "0.0" because isnumeric does not evaluate to True
            if '.' in dollars:
                try:
                    dollars = float(dollars)
                    return Decimal(dollars)
                except:
                    pass
            ###########################
            raise ValueError(f"dollars is of type string and not numeric")
        
        else:
            dollars = float(dollars)
    #################################################################################################

    return Decimal(dollars)

"""
Q5:
Adding cents would increase the number of return types, which would unfortunately increase the amount of downstream handling
A separate function should be used, given the simplicity of this code logic.  
if a candidate gets this wrong, it's not a dealbreaker, but it shows that his/her design is suboptimal.  

The second best solution is if he/she decides to incorporate this as an argument, the solution is to multiply the in_dollars by 100.  Ensure that the candidate
will now return as an int.  

Pro: 
- useful when downstream calculations requrie integer math or cents unit

Con:
- mixing return types (Decimal and int)
- better to have keep the functionality simple and not add complexity

Potential implementation: add a parameter (as_cents=False) and return as cents if True + document the behavior!
"""

if __name__ == "__main__":
    for _input in (None, "0", 0, 0.0):
        answer = to_decimal(_input)
        assert answer == Decimal(0)
        assert isinstance(answer, Decimal)

    # extra credit: handling string floats "41.96"
        # assert to_decimal("0.0") == Decimal(0)