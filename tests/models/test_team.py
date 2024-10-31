import pytest
from src.models.team import Team

@pytest.fixture
def team():
    return Team("Lions")

def test_team_creation(team):
    assert team.name == "Lions"
    assert team.points == 0
    assert team.wins == 0
    assert team.draws == 0
    assert team.losses == 0

def test_team_add_win(team):
    team.add_win()
    assert team.points == 3
    assert team.wins == 1
    assert team.draws == 0
    assert team.losses == 0

def test_team_add_draw(team):
    team.add_draw()
    assert team.points == 1
    assert team.wins == 0
    assert team.draws == 1
    assert team.losses == 0

def test_team_add_loss(team):
    team.add_loss()
    assert team.points == 0
    assert team.wins == 0
    assert team.draws == 0
    assert team.losses == 1

def test_team_multiple_results(team):
    team.add_win()    # 3 points
    team.add_draw()   # 1 point
    team.add_loss()   # 0 points
    
    assert team.points == 4
    assert team.wins == 1
    assert team.draws == 1
    assert team.losses == 1

def test_team_equality():
    team1 = Team("Lions")
    team2 = Team("Lions")
    team3 = Team("Snakes")
    
    team1.add_win()  # 3 points
    team2.add_win()  # 3 points
    team3.add_win()  # 3 points
    
    assert team1 == team2  # Same name and points
    assert team1 != team3  # Different name, same points

def test_team_string_representation(team):
    team.add_win()
    expected = f"Team(name='Lions', points=3, wins=1, draws=0, losses=0)"
    assert str(team) == expected
    assert repr(team) == expected


def test_team_stats_tracking():
    team = Team("Lions")
    
    team.add_win()
    assert team.matches_played == 1
    assert team.points == 3
    
    team.add_draw()
    assert team.matches_played == 2
    assert team.points == 4
    
    team.add_loss()
    assert team.matches_played == 3
    assert team.points == 4

def test_team_comparison():
    team1 = Team("Lions")
    team2 = Team("Snakes")
    
    team1.add_win()  # 3 points
    team2.add_draw() # 1 point
    
    # Test points comparison
    assert team1 > team2  # More points should come first
    assert team2 < team1
    assert not team1 < team2
    assert not team2 > team1
    
    # Test alphabetical ordering when points are equal
    team3 = Team("Antelopes")
    team3.add_win()  # 3 points, same as Lions
    assert team3 < team1  # Antelopes comes before Lions alphabetically
    assert team1 > team3  # Lions comes after Antelopes alphabetically
    
    # Test multiple teams with same points
    team4 = Team("Zebras")
    team4.add_win()  # 3 points
    assert team3 < team1 < team4  # Alphabetical order: Antelopes, Lions, Zebras

def test_team_comparison_edge_cases():
    team1 = Team("Lions")
    team2 = Team("Lions")  # Same name
    
    assert not team1 < team2  # Same name and points
    assert not team1 > team2
    assert team1 == team2
    
    team1.add_win()  # 3 points
    assert team1 > team2  # Same name but different points
    assert team2 < team1