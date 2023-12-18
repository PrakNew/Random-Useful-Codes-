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



# Method 2 for parsing in pydantic model
data = {"minimum":10,"maximum":2000}
try:
    model = Followers.parse_obj(data)
    print(model.dict())
except ValidationError as e:
    print(e)



#More precise example 

from typing import Optional, List, Union
from datetime import datetime, timezone
from dateutil.parser import parse as dt_parser
import uuid

import orjson
from pydantic import (
    validator,
    root_validator,
    Field,
    BaseModel as PydanticBaseModel,
)

from modules.common.loggers import STACKTRACE_LOGGER, COMMON_LOGGER


# -- HELPERS --
def orjson_dumps(v, *, default):
    # orjson.dumps returns bytes, to match standard json.dumps we need to decode
    return orjson.dumps(v, default=default).decode()


def check_datetime_format(v: Union[str, datetime]):
    if not v or v in ("", None):
        return v

    if not isinstance(v, datetime):
        try:
            v = dt_parser(v)
        except Exception as error:
            STACKTRACE_LOGGER.warning(error)
            raise ValueError(f"Unsupported date[time] format: {v}")
    if not v.tzinfo:
        v = v.replace(tzinfo=timezone.utc)
    return v


def remove_leading_special_chars(v: Union[str, List[str]]):
    print("V:", v)
    if not v or v in ("", None):
        return v

    if isinstance(v, list):
        v = [_v.lstrip("#@") for _v in v]
    else:
        v = v.lstrip("#@")
    print("V:", v)
    return v


# -- MODELS --
class BaseModel(PydanticBaseModel):
    class Config:
        json_loads = orjson.loads
        json_dumps = orjson_dumps


class AccountsRecord(BaseModel):
    uid: str
    account_type: str
    account_type_name: str
    creds_type: str
    status: str
    creds: dict
    config: Optional[dict]
    is_locked: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    @root_validator(pre=True)
    def create_unique_id(cls, values):
        hash_text = (
            values.get("account_type", "")
            + values.get("account_type_name")
            + values.get("creds", {}).get("account_name", "")
        )
        hash_value = uuid.uuid5(uuid.NAMESPACE_URL, hash_text)
        values["uid"] = hash_value
        return values

    _format_dates = validator("created_at", "updated_at", pre=True, allow_reuse=True)(
        check_datetime_format
    )

