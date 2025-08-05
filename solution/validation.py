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
