from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from todomanager.entities.enums import TaskPriority


@dataclass
class Task:
    id: int
    name: str
    priority: TaskPriority
    deadline: Optional[datetime]
    status: bool = False
