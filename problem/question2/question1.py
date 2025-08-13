from typing import Optional
import logging
from decimal import Decimal

logger = logging.getLogger(__name__)

def to_decimal(dollars: Optional[int | float | str]) -> Decimal:

    if not dollars: # account for zero ints/floats, empty strings.  
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
            raise ValueError(f"dollars is of type string and not numeric")
        
        else:
            dollars = float(dollars)

    return Decimal(dollars)