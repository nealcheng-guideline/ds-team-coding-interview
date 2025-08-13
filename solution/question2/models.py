"""
Location for pydantic base models
"""
from pydantic import BaseModel, field_validator
from decimal import Decimal
from typing import Optional
from question1 import to_decimal

class Participant(BaseModel):
    user_id: int
    full_name: str
    salary_dollars: Decimal| float

    def remove_full_name(self):
        self.full_name = ""

    def model_dump(self, *args, **kwargs):
        """ in order to convert the decimal back to a string during serialization to json"""
        model_dump = super().model_dump(*args, **kwargs)
        model_dump['salary_dollars'] = str(model_dump['salary_dollars'])
        return model_dump

    # this is optional and an extra credit.  If can't do this, please 
    # implement after data loading
    # @field_validator("salary_dollars")
    # def fix_null_salary(cls, salary: Optional[float]):
    #     return to_decimal(salary)