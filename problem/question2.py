"""
For this exercise, you will use the function you had written from part 1 to ensure that the "salary_dollars"
field will not break the LLM pipeline.  

1. Load data from file
2. Fill in a Participant Pydantic BaseModel
3. Use to_decimal to perform type coercion validation for the inputs
4. Serialize Pydantic models for providing context to prompt 
5. Initialize the GeminiClient and make a call.  
"""

from question1 import to_decimal
from copy import deepcopy
from validation import validate_model_input, validate_prompt_input
from dotenv import load_dotenv
from errors import ValidationError, PromptError
from models import Participant
load_dotenv()



class GeminiClient():
    
    def __init__(self, api_key: str, model: str, temperature: float):
        try:
            validate_model_input(api_key, model, temperature)
        except ValueError as e:
            raise ValidationError("Model input validation had failed") from e

    def make_query(self, prompt: str):
        if not prompt:
            raise Exception("Error: Prompt is not given")

        return """
        Sure I can definitely give it a shot!  Please provide me with additional information about
        1. Whether there is employer match, and if so, to what extent.  
        2. The breakdown of Highly Compensated Employees (HCE) vs Non-Highly Compensated Employees (NHCE)
        """ 

def construct_prompt(participants: list[Participant]) -> str:
    try:
        validate_prompt_input(participants)
    except TypeError as e:
        raise PromptError("Prompt contruction had failed") from e
 

    # removing full_name to ensure we do not provide PII to the LLM
    participant_copy = deepcopy(participants)

    for participant in participant_copy:
        participant.full_name = ""
        
    template = """You are a financial accountant with 20 years of experience working within large firms
    such as Deloitte and PwC.  Can you please construct a recommendation for suitable 401k options for the employees within
    this legal entity?
    (Please note that participants will be denoted by user_id, which is their unique identifier):

     {{Enter participant information here!}} """
    
    print("Prompt:\n")
    print(template)
    print("\n")

    return template


def main():
    pass
    # Load Data


    # Initialize GeminiClient and make query



if __name__ == "__main__":
    main()
