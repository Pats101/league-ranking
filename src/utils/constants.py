"""Game scoring and validation constants"""

# Points
POINTS_FOR_WIN = 3
POINTS_FOR_DRAW = 1
POINTS_FOR_LOSS = 0

# Commands
EXIT_COMMAND = "done"
MATCH_FORMAT = "Team1 Score1, Team2 Score2"

# Error 
INVALID_MATCH_FORMAT = f"Bad format. Expected: {MATCH_FORMAT}"
NEGATIVE_SCORE_ERROR = "Scores must be positive"
EMPTY_TEAM_ERROR = "Team name required"
