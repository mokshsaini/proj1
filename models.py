from pydantic import BaseModel, Field
from datetime import date, datetime
from typing import Optional

class Records(BaseModel):
    Name: str 
    Date: date
    BP: str
    Weight_in_kg: float
    Gender: str
    Height_in_meters: float
    Fever: bool = False

    def date_conversion(self):
        if self.Date:
            self.Date = datetime.strptime(str(self.Date), '%Y-%m-%d')


class Records_fetch(BaseModel):
    Name: str 
    Date: Optional[date] = None
    BP: Optional[str] = None
    Weight_in_kg: Optional[float] = None
    Gender: Optional[str] = None
    Height_in_meters: Optional[float] = None
    Fever: bool = Field(default = False)

    def date_conversion(self):
        if self.Date:
            self.Date = datetime.strptime(str(self.Date), '%Y-%m-%d')

