from dataclasses import dataclass
from typing import Tuple

@dataclass
class Match:
    """Represents a match between two teams with their scores"""
    def __init__(self, team1: str, score1: int, team2: str, score2: int):
        if score1 < 0 or score2 < 0:
            raise ValueError("Match scores cannot be negative")
        self.team1 = team1
        self.score1 = score1
        self.team2 = team2
        self.score2 = score2
        
    @property
    def home_team(self) -> str:
        return self.team1
        
    @property
    def away_team(self) -> str:
        return self.team2
        
    @property
    def home_score(self) -> int:
        return self.score1
        
    @property
    def away_score(self) -> int:
        return self.score2
    
    def __repr__(self):
        return f"Match(team1='{self.team1}', score1={self.score1}, team2='{self.team2}', score2={self.score2})"

    def __post_init__(self) -> None:
        """Validate match data after initialization"""
        if self.score1 < 0 or self.score2 < 0:
            raise ValueError("Scores cannot be negative")
        if not self.team1 or not self.team2:
            raise ValueError("Team names cannot be empty")
    
    @property
    def result(self) -> Tuple[str, str, str]:
        """Returns (winner, loser, result_type) or (team1, team2, 'draw')"""
        if self.home_score > self.away_score:
            return (self.home_team, self.away_team, 'win')
        elif self.away_score > self.home_score:
            return (self.away_team, self.home_team, 'win')
        return (self.home_team, self.away_team, 'draw')