from question1 import to_decimal
import json
from copy import deepcopy
import os



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
 
    participant_copy = deepcopy(participants)

    # removing full_name to ensure we do not provide PII to the LLM
    # or the interviewee can use the Field(exclude=True) from Pydantic
    for participant in participant_copy:
        participant.full_name = ""
        
    template = f"""You are a financial accountant with 20 years of experience working within large firms
    such as Deloitte and PwC.  Can you please construct a recommendation for suitable 401k options for the employees within
    this legal entity?
    (Please note that participants will be denoted by user_id, which is their unique identifier):
     {[participant.model_dump() for participant in participant_copy]} """
    
    print("Prompt:\n")
    print(template)
    print("\n")

    return template


def main():
    with open('data.json') as f:
        data = json.load(f)

    participant_list = []
    for participant in data['participants']:
        participant['salary_dollars']= to_decimal(participant['salary_dollars'])
        participant_list.append(Participant(**participant))

    api_key = os.getenv("API_KEY")
    temperature = float(os.getenv("MODEL_TEMPERATURE")) # adding float here is very important, as env variables are strings when loaded!
    llm_model = os.getenv("MODEL_NAME")

    prompt = construct_prompt(participant_list)

    # implement the Gemini client and make an API call
    llm_client = GeminiClient(api_key=api_key, model=llm_model, temperature=temperature)
    llm_answer = llm_client.make_query(prompt)  
    print("Gemini Response:\n")
    print(llm_answer)

# Extra credit:
# We want to design a function to filter participants by their user_ids.  Can you write such a function?

# Extra credit question:
# If we are to perform frequent filtering by user_id, what changes would you recommend to this workflow?

def filter_participants(participants: list[Participant], desired_user_ids: list[int]):
    desired_user_ids = set(desired_user_ids) # to account for duplicates and fast look-up
    return list(filter(lambda participant: participant.user_id in desired_user_ids, participants))


if __name__ == "__main__":
    main()


