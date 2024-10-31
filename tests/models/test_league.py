import pytest
from src.models.league import League
from src.models.match import Match
from src.models.team import Team

@pytest.fixture
def league():
    return League()

@pytest.fixture
def sample_matches():
    return [
        Match("Lions", 3, "Snakes", 3),      # Draw
        Match("Tarantulas", 1, "FC Awesome", 0),  # Tarantulas win
        Match("Lions", 1, "FC Awesome", 1),   # Draw
        Match("Tarantulas", 3, "Snakes", 1),  # Tarantulas win
        Match("Lions", 4, "Grouches", 0)      # Lions win
    ]

def test_league_creation(league):
    assert len(league.teams) == 0

def test_add_single_match(league):
    match = Match("Lions", 3, "Snakes", 2)
    league.add_match(match)
    
    assert len(league.teams) == 2
    assert "Lions" in league.teams
    assert "Snakes" in league.teams
    assert league.teams["Lions"].points == 3  # Win
    assert league.teams["Snakes"].points == 0  # Loss

def test_add_draw_match(league):
    match = Match("Lions", 3, "Snakes", 3)
    league.add_match(match)
    
    assert league.teams["Lions"].points == 1  # Draw
    assert league.teams["Snakes"].points == 1  # Draw

def test_multiple_matches(league, sample_matches):
    for match in sample_matches:
        league.add_match(match)
    
    rankings = league.get_rankings()
    assert len(rankings) == 5  # 5 unique teams
    
    # Verify Tarantulas are first (6 points from 2 wins)
    assert rankings[0].name == "Tarantulas"
    assert rankings[0].points == 6

def test_rankings_sort_order(league):
    # Add matches to create specific point scenarios
    matches = [
        Match("Team A", 2, "Team B", 0),  # A wins (3 points)
        Match("Team C", 2, "Team D", 2),  # Both get 1 point
        Match("Team B", 1, "Team C", 1),  # Both get 1 point
    ]
    
    for match in matches:
        league.add_match(match)
    
    rankings = league.get_rankings()
    
    # Check points order
    assert rankings[0].name == "Team A"  # 3 points
    assert rankings[1].name == "Team C"  # 2 points
    assert rankings[2].name == "Team B"  # 1 point
    assert rankings[3].name == "Team D"  # 1 point

def test_empty_rankings(league):
    rankings = league.get_rankings()
    assert len(rankings) == 0
    assert isinstance(rankings, list)
    