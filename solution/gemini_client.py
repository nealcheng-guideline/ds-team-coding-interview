"""
Location for GeminiClient
"""
from validation import validate_model_input
from errors import ValidationError

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