import pytest
from src.models.match import Match

@pytest.fixture
def sample_match():
    return Match("Lions", 3, "Snakes", 2)

def test_match_creation():
    match = Match("Lions", 3, "Snakes", 2)
    assert match.team1 == "Lions"
    assert match.score1 == 3
    assert match.team2 == "Snakes"
    assert match.score2 == 2

def test_match_properties(sample_match):
    assert sample_match.home_team == "Lions"
    assert sample_match.away_team == "Snakes"
    assert sample_match.home_score == 3
    assert sample_match.away_score == 2

def test_match_string_representation(sample_match):
    expected = "Match(team1='Lions', score1=3, team2='Snakes', score2=2)"
    assert str(sample_match) == expected
    assert repr(sample_match) == expected

def test_match_invalid_scores():
    with pytest.raises(ValueError):
        Match("Lions", -1, "Snakes", 0)
    with pytest.raises(ValueError):
        Match("Lions", 0, "Snakes", -1)        
    with pytest.raises(ValueError, match="scores cannot be negative"):
        Match("Lions", -1, "Snakes", -1)

def test_match_edge_cases():
    # Test zero scores (should be valid)
    match = Match("Lions", 0, "Snakes", 0)
    assert match.score1 == 0
    assert match.score2 == 0
    
    # Test large scores (should be valid)
    match = Match("Lions", 100, "Snakes", 100)
    assert match.score1 == 100
    assert match.score2 == 100
