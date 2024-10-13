from pydantic import BaseModel
from typing import List, Dict


class TranslationRequest(BaseModel):
    text: str
    languagues: List[str]


class TaskResponse(BaseModel):
    task_id: int


class TranstaltionStatus(BaseModel):
    status: int
    status: str
    translation: Dict[str, str]