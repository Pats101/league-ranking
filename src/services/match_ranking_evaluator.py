from typing import List
from ..models.match import Match
from ..models.league import League
from ..models.team import Team

class MatchRankingEvaluator:
    @staticmethod
    def calculate_rankings(matches: List[Match]) -> List[Team]:
        league = League()
        for match in matches:
            league.add_match(match)
        return league.get_rankings()