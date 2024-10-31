from typing import List
from ..models.match import Match
from ..utils.constants import INVALID_MATCH_FORMAT
import logging

logger = logging.getLogger(__name__)

class GameDataAnalyzer:
    @staticmethod
    def parse_line(line: str) -> Match:
        """Converts a match result line into a Match object"""
        try:
            team1, team2 = line.split(',')
            
            # Get name and score for each team
            name1, score1 = team1.strip().rsplit(' ', 1)
            name2, score2 = team2.strip().rsplit(' ', 1)
            
            return Match(
                name1.strip(), 
                int(score1),
                name2.strip(), 
                int(score2)
            )
        except (ValueError, IndexError):
            raise ValueError(INVALID_MATCH_FORMAT)

    
    @staticmethod
    def parse_file(file_path: str) -> List[Match]:
        """Parse match results from a file"""
        matches = []
        with open(file_path, 'r') as f:
            for line in f:
                if line.strip():
                    matches.append(GameDataAnalyzer.parse_line(line))
        return matches