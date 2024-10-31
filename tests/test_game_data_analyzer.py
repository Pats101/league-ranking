import pytest
from src.services.game_data_analyzer import GameDataAnalyzer


def test_parse_valid_match():
    parser = GameDataAnalyzer()
    match = parser.parse_line("Lions 3, Snakes 3")
    assert match.team1 == "Lions"
    assert match.score1 == 3
    assert match.team2 == "Snakes"
    assert match.score2 == 3

def test_parse_invalid_match():
    parser = GameDataAnalyzer()
    with pytest.raises(ValueError):
        parser.parse_line("Invalid Format")

def test_parse_match_result():
    parser = GameDataAnalyzer()
    result = parser.parse_line("Lions 3, Snakes 3")
    
    assert result is not None
    assert result.team1 == "Lions"
    assert result.team2 == "Snakes"
    assert result.score1 == 3
    assert result.score2 == 3

def test_invalid_match_format():
    parser = GameDataAnalyzer()
    with pytest.raises(ValueError):
        parser.parse_line("Invalid Format")