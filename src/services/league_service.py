from typing import Dict, List, Tuple
import logging
from collections import defaultdict

from src.models.match import Match
from src.models.team import Team
from src.utils.constants import (
    POINTS_FOR_WIN,
    POINTS_FOR_DRAW,
    POINTS_FOR_LOSS
)

logger = logging.getLogger(__name__)

class LeagueService:
    """Service to manage league standings and rankings"""
    
    def __init__(self) -> None:
        self.teams: Dict[str, Team] = defaultdict(lambda: Team(""))
        logger.info("Initialized new league")

    def process_match(self, match: Match) -> None:
        """Updates team standings based on match result"""        
        # Get or create teams
        team1 = self._get_or_create_team(match.team1)
        team2 = self._get_or_create_team(match.team2)
        
        # Calculate and award points
        if match.score1 > match.score2:  # Team 1 wins
            team1.add_points(POINTS_FOR_WIN)
            team2.add_points(POINTS_FOR_LOSS)
        elif match.score2 > match.score1:  # Team 2 wins
            team1.add_points(POINTS_FOR_LOSS)
            team2.add_points(POINTS_FOR_WIN)
        else:  # Draw
            team1.add_points(POINTS_FOR_DRAW)
            team2.add_points(POINTS_FOR_DRAW)

    TeamRanking = Tuple[int, str, int]  # rank, name, points

    def get_rankings(self) -> List[TeamRanking]:
        """Get the current rankings of all teams, sorted by points (descending) and name (alphabetically)"""
        if not self.teams:
            return []

        # Sort teams by points (descending) and name (alphabetically)
        sorted_teams = sorted(
            self.teams.values(),
            key=lambda team: (-team.points, team.name)  # Negative points for descending order
        )
        
        # Generate rankings with proper handling of ties
        rankings: List[TeamRanking] = []
        current_rank = 1
        previous_points = None
        
        for i, team in enumerate(sorted_teams):
            if previous_points is not None and team.points != previous_points:
                current_rank = i + 1
            rankings.append((current_rank, team.name, team.points))
            previous_points = team.points
        return rankings
    

    def _get_or_create_team(self, team_name: str) -> Team:
        """Get an existing team or create a new one"""
        if team_name not in self.teams:
            self.teams[team_name] = Team(team_name)
        return self.teams[team_name]
    
    def clear(self) -> None:
        """Clear all teams and rankings"""
        self.teams.clear()

