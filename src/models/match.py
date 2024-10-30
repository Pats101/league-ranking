from dataclasses import dataclass
from typing import Tuple

@dataclass
class Match:
    """Represents a match between two teams with their scores"""
    team1: str
    score1: int
    team2: str
    score2: int

    def __post_init__(self) -> None:
        """Validate match data after initialization"""
