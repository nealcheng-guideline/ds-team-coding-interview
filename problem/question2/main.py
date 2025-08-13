"""
Prompt: Now you want to call an LLM (Gemini) to get a recommendation for a 401k plan given the participants.
To do this, you need to initalize the Participant objects (created with Pydantic) and then call the GeminiClient.
Modify and complete the code below to accomplish this:

1. Load the participant data
2. Initialize the Participant object ensuring that the correct type of "salary_dollars" is used
3. Serialize Pydantic models to provide context to the prompt 
4. Initialize the GeminiClient and make a call
"""
import os

from dotenv import load_dotenv

from utils import to_decimal
from models import Participant
from gemini_client import GeminiClient
from validation import validate_prompt_input

# This loads env variables
load_dotenv()


def construct_prompt(participants: list[Participant]) -> str:    
    # Validate the prompt input 
    validate_prompt_input(participants)

    # Remove full_name to ensure we do not provide PII to the LLM
    for participant in participants:
        participant.remove_full_name()

    # TODO: Serialize the Participant objects to JSON
 
    
    # TODO: Add this information to the prompt
    prompt = """You are a financial accountant with 20 years of experience working within large firms
    such as Deloitte and PwC.  Can you please construct a recommendation for suitable 401k options for the participants within
    this legal entity? 
    (Please note that participants will be denoted by user_id, which is their unique identifier): 

    {{Enter participant information here!}}
    """
    
    print("Prompt:\n")
    print(prompt)
    print("\n")

    return prompt


def execute_llm_pipeline() -> str:    
    # 1. Load data from "participant_data.json"

    # 2. Initialize the Participant objects ensuring that the correct type of "salary_dollars" is used 
    # participants = [Participant(**participant) for participant in data["participants"]] 

    # 3. Construct the prompt
    # prompt = construct_prompt(participants)

    # 4. Initialize the GeminiClient and uncomment to call the client
    # client = GeminiClient()
    # response = client.make_query(prompt)
    return ""

if __name__ == "__main__":
    llm_answer = execute_llm_pipeline()
    print("Gemini Response:\n")
    print(llm_answer)