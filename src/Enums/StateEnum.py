from enum import Enum


class StateEnum(Enum):
    START = 0
    RUNNING = 1
    FINISHED = 2
    ERROR = 3
    DOWN = 4
