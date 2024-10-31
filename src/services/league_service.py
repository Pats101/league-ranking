from typing import Dict
from collections import defaultdict

from src.models.team import Team

class LeagueService:
    """Service to manage league standings and rankings"""
    
    def __init__(self) -> None:
        self.teams: Dict[str, Team] = defaultdict(lambda: Team(""))


