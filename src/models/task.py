
from dataclasses import dataclass
from datetime import datetime

state = ("to do", "in progress", "done")

@dataclass
class Task:
    id: int
    title: str
    description: str = ""
    state: str = state[0]
    created_at: datetime = datetime.now()
