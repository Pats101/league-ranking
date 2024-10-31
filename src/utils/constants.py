"""Constants used throughout the application"""
from typing import Final

# Points system
POINTS_FOR_WIN: Final[int] = 3
POINTS_FOR_DRAW: Final[int] = 1
POINTS_FOR_LOSS: Final[int] = 0

# Input/Output
EXIT_COMMAND: Final[str] = "done"
MATCH_FORMAT: Final[str] = "Team1 Score1, Team2 Score2"

# Error messages
INVALID_MATCH_FORMAT: Final[str] = f"Invalid match format. Expected format: {MATCH_FORMAT}"
NEGATIVE_SCORE_ERROR: Final[str] = "Scores cannot be negative"
EMPTY_TEAM_ERROR: Final[str] = "Team names cannot be empty"