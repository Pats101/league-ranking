from dataclasses import dataclass

@dataclass
class Team:
    name: str
    points: int = 0
    matches_played: int = 0
    wins: int = 0
    draws: int = 0
    losses: int = 0

    def __init__(self, name):
        self.name = name
        self.points = 0

