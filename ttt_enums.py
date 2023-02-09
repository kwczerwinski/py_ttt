from enum import IntEnum, StrEnum


class GameState(IntEnum):
    START = 0,
    IN_PROGRESS = 1,
    END = 2


class GridState(IntEnum):
    NOT_CONCLUDED = 0,
    WINNER = 1,
    DRAW = 2


class Sign(StrEnum):
    O = 'O',
    X = 'X'


class StatusCode(IntEnum):
    SUCCESS = 0,
    FAILURE = 1
