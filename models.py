from pydantic import BaseModel
from typing import Optional, List


class ListCheck(BaseModel):
    lists: List[int]
    status: Optional[bool]
