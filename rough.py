from datetime import datetime

# from pydantic import BaseModel


class User(x):
    id: int = 5
    name: str = "John Doe"
    signup_ts: datetime | None = None
    friends: list[int] = []


external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}
user = User()
print(user)
# > User id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, 3]
print(user.id)
# > 123


from datetime import datetime

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    signup_ts: datetime | None = None
    friends: list[int] = []


external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}
user = User(**external_data)
print(user)
# > User id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, 3]
print(user.id)
# > 123
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

d = {"a":True, "b":2.0, 'c':3.0}
print(records(d))