from dataclasses import dataclass
from enum import Enum
from datetime import datetime
from typing import Optional, Tuple


class TaskPriority(Enum):
    LOW = "Nízká"
    MID = "Střední"
    HIGH = "Vysoká"

    @classmethod
    def try_parse(cls, value: str) -> Tuple[bool, Optional["TaskPriority"]]:
        for priority in cls:
            if priority.value == value:
                return True, priority
        return False, None


@dataclass
class Task:
    Id: int
    Name: str
    Priority: TaskPriority
    DueDate: Optional[datetime]
    IsDone: bool = False
