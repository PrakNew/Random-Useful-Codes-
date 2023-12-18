from typing import Callable, Optional, Type, List, Any, Union
from pydantic import BaseModel, Field, EmailStr, constr, conint, validator
from datetime import datetime
class Influencers(BaseModel):
    minimum: int
    maximum: int

    @validator('maximum')
    def minimum_less_than_maximum(cls, v, values):
        if 'minimum' in values and v < values['minimum']:
            raise ValueError('maximum must be greater than minimum')
        return v
class DateRange(BaseModel):
    influencers: Optional[Influencers] = {}
    start_date: datetime
    end_date: datetime

    @validator('end_date')
    def end_dateafter_from(cls, v, values):
        if 'start_date' in values and v <= values['start_date']:
            raise ValueError('end date must be after start date')
        return v
    
    @validator('start_date', 'end_date', pre=True)
    def check_datetime_format(cls, v):
        if isinstance(v, str):
            return datetime.fromisoformat(v)
        return v

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, validator

class DateRange(BaseModel):
    from_date: Optional[datetime]
    to_date: Optional[datetime]
    
    @validator('from_date', 'to_date', pre=True)
    def parse_date(cls, v):
        if isinstance(v, datetime):
            return v
        try:
            return datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%fZ')
        except ValueError:
            return datetime.strptime(v, '%Y-%m-%d')


d={
    "from_date" : "2022-02-21T00:00:00.000Z",
    "to_date":"2022-02-21"
}

# result = DateRange(**d)
# print(result.dict())

class Followers(BaseModel):
    minimum: int
    maximum: int

    @validator('maximum')
    def minimum_less_than_maximum(cls, v, values):
        if 'minimum' in values and v < values['minimum']:
            raise ValueError('maximum must be greater than minimum')
        return v
    
result = Followers(**{"minimum":10,"maximum":2000})
print(result)
data = {"minimum":10,"maximum":2000}
try:
    model = Followers.parse_obj(data)
    print(model.dict())
except ValidationError as e:
    print(e)
