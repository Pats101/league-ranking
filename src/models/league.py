from typing import Dict
from .team import Team

class League:
    def __init__(self):
        self.teams: Dict[str, Team] = {}
    