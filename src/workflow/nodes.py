from typing_extensions import TypedDict
from 

class State(TypedDict):
    dolar: float
    notices: str
    yahoo_finance: str
    combined_output: str

class Workflow:
    
    @staticmethod
    def dolar(state: State):
        return{"dolar": ""}
    
    