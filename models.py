from pydantic import BaseModel
from datetime import date

class records(BaseModel):
    Name: str
    Date: str
    BP: str
    Weight_in_kg: str
    Gender: str
    Height_in_meters: str
    Fever: str = 'False'