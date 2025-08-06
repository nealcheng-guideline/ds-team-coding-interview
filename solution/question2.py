"""
Now you want to call LLM (Gemini) to get a recommendation for a 401k plan given the participants.
To do so, you need to initalize the Participant object (created with Pydantic) and then call the GeminiClient.
Modify and fill in the code below to do so. 

1. Load the participant data
2. Initialize the Participant object making sure that the correct type of "salary_dollars" is used (Hint: use to_decimal from question1.py)
3. Serialize Pydantic models for providing context to prompt 
4. Initialize the GeminiClient and make a call.  
"""
import os

from dotenv import load_dotenv

from question1 import to_decimal
from models import Participant
from gemini_client import GeminiClient
from validation import validate_prompt_input
from errors import PromptError

load_dotenv()


def construct_prompt(participants: list[Participant]) -> str:
    try:
        validate_prompt_input(participants)
    except TypeError as e:
        raise PromptError("Prompt contruction had failed") from e
    
    # Remove full_name to ensure we do not provide PII to the LLM
    for participant in participants:
        participant.remove_full_name()

    template = f"""You are a financial accountant with 20 years of experience working within large firms
    such as Deloitte and PwC.  Can you please construct a recommendation for suitable 401k options for the employees within
    this legal entity?
    (Please note that participants will be denoted by user_id, which is their unique identifier):
     {[participant.model_dump() for participant in participants]} """
    
    print("Prompt:\n")
    print(template)
    print("\n")

    return template


def main():
    import json
    # 1. Load Data from "data.json"
    with open('participant_data.json') as f:
        data = json.load(f)

    # 2. Fix this to initialize a list of Participant objects
    participants = []
    for participant in data['participants']:
        participant['salary_dollars'] = to_decimal(participant['salary_dollars'])
        participants.append(Participant(**participant))

    # 3. Construct the prompt
    prompt = construct_prompt(participants)

    # 4. Initialize GeminiClient and uncomment to call the client
    api_key = os.getenv("API_KEY")
    temperature = float(os.getenv("MODEL_TEMPERATURE")) # adding float here is very important, as env variables are strings when loaded!
    llm_model = os.getenv("MODEL_NAME")
    client = GeminiClient(api_key=api_key, model=llm_model, temperature=temperature)
    response = client.make_query(prompt)  
    print("Gemini Response:\n")
    print(response)
    
"""
Extra credit:
1. We want to design a function to filter participants by their user_ids.  Can you write such a function?
2. If we are to perform frequent filtering by user_id, what changes would you recommend to this workflow?
"""
def filter_participants(participants: list[Participant], desired_user_ids: list[int]):
    desired_user_ids = set(desired_user_ids) # to account for duplicates and fast look-up
    return list(filter(lambda participant: participant.user_id in desired_user_ids, participants))


if __name__ == "__main__":
    main()


