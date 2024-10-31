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
        logger.info("New league started")

    def process_match(self, match: Match) -> None:
        """Updates team standings based on match result"""        
        # Get or create teams
        team1 = self._get_team(match.team1)
        team2 = self._get_team(match.team2)
        
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

    def get_rankings(self) -> List[Tuple[int, str, int]]:
        """Get the current rankings of all teams, sorted by points (descending) and name (alphabetically)"""
        if not self.teams:
            return []

        # Sort teams by points (descending) and name (alphabetically)
        sorted_teams = sorted(
            self.teams.values(),
            key=lambda t: (-t.points, t.name)  # Negative points for descending order
        )
        
        # Generate rankings with proper handling of ties
        rankings = []
        rank = 1
        prev_pts = None
        
        for i, team in enumerate(sorted_teams):
            if prev_pts is not None and team.points != prev_pts:
                rank = i + 1
            rankings.append((rank, team.name, team.points))
            prev_pts = team.points
        return rankings
    

    def _get_team(self, name: str) -> Team:
        """Get an existing team or create a new one"""
        if name not in self.teams:
            self.teams[name] = Team(name)
        return self.teams[name]
    
    def clear(self) -> None:
        """Clear all teams and rankings"""
        self.teams.clear()

