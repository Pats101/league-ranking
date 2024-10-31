import pytest
from src.models.match import Match

@pytest.fixture
def match():
    return Match("Lions", 3, "Snakes", 2)

def test_match_creation():
    match = Match("Lions", 3, "Snakes", 2)
    assert match.team1 == "Lions"
    assert match.score1 == 3
    assert match.team2 == "Snakes"
    assert match.score2 == 2

def test_string_format(match):
    assert str(match) == "Lions 3, Snakes 2"

def test_invalid_scores():
    with pytest.raises(ValueError):
        Match("Lions", -1, "Snakes", 0)
    with pytest.raises(ValueError):
        Match("Lions", 0, "Snakes", -1)

def test_zero_score_match():
    match = Match("Lions", 0, "Snakes", 0)
    assert match.score1 == match.score2 == 0
