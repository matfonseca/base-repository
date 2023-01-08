from json import loads
from typing import Optional, List
from pydantic import BaseModel


class ProjectAbandonment(BaseModel):
    pa_id: Optional[str]
    pid: str
    tid: str
    reasons: List[str]

    def to_json(self):
        return loads(self.json(exclude_defaults=True))
