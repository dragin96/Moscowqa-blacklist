from typing import List
from pydantic import BaseModel

class BlacklistUser(BaseModel):
    first_name: str
    last_name: str
    phone_numbers: List[str]
    emails: List[str]
    telegrams: List[str]
    comment: str