from datetime import date
from pydantic import BaseModel
class records(BaseModel):
    Fever: bool
    Weight_in_kg: float
    Height_in_meters: float
    Date: date
r = records()
r.Date=230324
print(r[Date])