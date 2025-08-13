"""
Location for GeminiClient
"""
from validation import validate_model_input

class GeminiClient():
    def __init__(self, api_key: str, model_name: str, model_temperature: float):
        validate_model_input(api_key, model_name, model_temperature)
        
        self.api_key = api_key
        self.model_name = model_name
        self.model_temperature = model_temperature

    def make_query(self, prompt: str):
        if not prompt:
            raise Exception("Error: Prompt is not given")

        return """
        Sure I can definitely give it a shot!  Please provide me with additional information about
        1. Whether there is employer match, and if so, to what extent.  
        2. The breakdown of Highly Compensated Employees (HCE) vs Non-Highly Compensated Employees (NHCE)
        """