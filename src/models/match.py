from dataclasses import dataclass
from typing import Tuple
from ..utils.constants import EMPTY_TEAM_ERROR, NEGATIVE_SCORE_ERROR

@dataclass
class Match:
    """Represents a match between two teams with their scores"""
    team1: str
    score1: int
    team2: str
    score2: int

    def __post_init__(self) -> None:
        """Validate match data after initialization"""
        if self.score1 < 0 or self.score2 < 0:
            raise ValueError(NEGATIVE_SCORE_ERROR)
        if not self.team1 or not self.team2:
            raise ValueError(EMPTY_TEAM_ERROR)
    
    def __str__(self) -> str:
        return f"{self.team1} {self.score1}, {self.team2} {self.score2}"
    
    def __repr__(self) -> str:
        return f"Match(team1='{self.team1}', score1={self.score1}, team2='{self.team2}', score2={self.score2})"
        
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
    
    @property
    def result(self) -> Tuple[str, str, str]:
        """Returns (winner, loser, result_type) or (team1, team2, 'draw')"""
        if self.home_score > self.away_score:
            return (self.home_team, self.away_team, 'win')
        elif self.away_score > self.home_score:
            return (self.away_team, self.home_team, 'win')
        return (self.home_team, self.away_team, 'draw')