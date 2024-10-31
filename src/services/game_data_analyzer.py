from typing import List
from ..models.match import Match
from ..utils.constants import INVALID_MATCH_FORMAT
import logging

logger = logging.getLogger(__name__)

class GameDataAnalyzer:
    @staticmethod
    def parse_line(line: str) -> Match:
        """
        Parse a line of match result into a Match object
        
        Args:
            line: String in format "Team1 Score1, Team2 Score2"
            
        Returns:
            Match object representing the parsed data
            
        Raises:
            ValueError: If the line format is invalid
        """
        logger.debug(f"Parsing line: {line}")
        
        try:
            team1_info, team2_info = line.split(',')
        except ValueError:
            logger.error(f"Invalid line format: {line}")
            raise ValueError(INVALID_MATCH_FORMAT)

        try:
            # Parse team1
            team1_parts = team1_info.strip().rsplit(' ', 1)
            if len(team1_parts) != 2:
                raise ValueError("Invalid team1 format")
            team1_name = team1_parts[0].strip()
            team1_score = int(team1_parts[1])

            # Parse team2
            team2_parts = team2_info.strip().rsplit(' ', 1)
            if len(team2_parts) != 2:
                raise ValueError("Invalid team2 format")
            team2_name = team2_parts[0].strip()
            team2_score = int(team2_parts[1])

            match = Match(team1_name, team1_score, team2_name, team2_score)
            logger.debug(f"Successfully parsed match: {match}")
            return match

        except (ValueError, IndexError) as e:
            logger.error(f"Error parsing match: {str(e)}")
            raise ValueError(f"Invalid match format: {str(e)}")

    
    @staticmethod
    def parse_file(file_path: str) -> List[Match]:
        """Parse match results from a file"""
        matches = []
        with open(file_path, 'r') as f:
            for line in f:
                if line.strip():
                    matches.append(GameDataAnalyzer.parse_line(line))
        return matches