from .team import Team
from .match import Match
from typing import Dict, List

class League:
    def __init__(self):
        self.teams: Dict[str, Team] = {}
        
    def add_match(self, match: Match):
        # Ensure teams exist
        if match.home_team not in self.teams:
            self.teams[match.home_team] = Team(match.home_team)
        if match.away_team not in self.teams:
            self.teams[match.away_team] = Team(match.away_team)
            
        # Update team statistics
        home_team = self.teams[match.home_team]
        away_team = self.teams[match.away_team]
        
        if match.home_score > match.away_score:
            home_team.add_win()
            away_team.add_loss()
        elif match.home_score < match.away_score:
            home_team.add_loss()
            away_team.add_win()
        else:
            home_team.add_draw()
            away_team.add_draw()
    
    def get_rankings(self) -> List[Team]:
        return sorted(
            self.teams.values(),
            key=lambda x: (-x.points, x.name)  # Sort by points (desc) and then name (asc)
        )
    