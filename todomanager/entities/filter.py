from enum import Enum
from typing import Optional, Tuple


class Filter(Enum):
    Priority = "priorita"
    Status = "stav"

    @classmethod
    def try_parse(cls, value: str) -> Tuple[bool, Optional["Filter"]]:
        for filter in cls:
            if filter.value == value:
                return True, filter
        return False, None
