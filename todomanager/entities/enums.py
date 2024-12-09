from enum import Enum
from typing import Optional, Tuple


class Command(Enum):
    ADD = "add"
    LIST = "list"
    REMOVE = "remove"
    COMPLETE = "complete"
    EDIT = "edit"
    SAVE = "save"
    EXIT = "exit"

    @classmethod
    def try_parse(cls, value: str) -> Tuple[bool, Optional["Command"]]:
        for command in cls:
            if command.value == value:
                return True, command
        return False, None


class Filter(Enum):
    PRIORITY = "priorita"
    STATUS = "stav"

    @classmethod
    def try_parse(cls, value: str) -> Tuple[bool, Optional["Filter"]]:
        for filter in cls:
            if filter.value == value:
                return True, filter
        return False, None


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
