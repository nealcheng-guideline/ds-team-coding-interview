from models import Participant
import base64


def validate_model_input(api_key: str, model:str, temperature: float):
        if api_key != base64.b64decode("d2VmYWVmd2FmZXdm").decode('utf-8'): # supposed to be model key
            raise ValueError("Api key is not properly set")

        if model != "gemini-2.5-flash":
            raise ValueError("The model name is not correct")

        if not isinstance(temperature, float):
            raise ValueError("Model temperature is not of the right type")
        else:
             if not temperature > 0.0:
                  raise ValueError("Temperature cannot be negative")

def validate_prompt_input(participants: list[Participant]):
    if not all(isinstance(participant, Participant) for participant in participants):
        raise TypeError("The argument for construct_prompt has to be a list of instance <Participants>")
  
    
def validate_query(prompt: str):
    if not prompt:
         raise Exception("Error: Prompt is not given")
    
    condition1 = "202" not in prompt
    condition2 = "205" not in prompt
    if condition1 or condition2:
        raise Exception("One or more user_id not present")

    condition3 = "4000" not in prompt
    condition4 = "'0'" not in prompt

    if condition3 or condition4:
         raise Exception("One or more salary information not in prompt")
    
    condition4 = "John Smith" in prompt
    condition5 = "Jane Schoo" in prompt

    if condition4 or condition5:
         raise Exception("PII in prompt")
