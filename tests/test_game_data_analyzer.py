import pytest
from src.services.game_data_analyzer import GameDataAnalyzer

def test_parse_match():
    a = GameDataAnalyzer()
    result = a.parse_line("Lions 3, Snakes 3")
    
    assert result.team1 == "Lions"
    assert result.score1 == 3
    assert result.team2 == "Snakes"
    assert result.score2 == 3

def test_invalid_format():
    a = GameDataAnalyzer()
    with pytest.raises(ValueError):
        a.parse_line("Invalid Format")

# Add more meaningful test cases like:
def test_parse_edge_cases():
    a = GameDataAnalyzer()
    with pytest.raises(ValueError):
        a.parse_line("Team A 999, Team B -1")  # unrealistic scores