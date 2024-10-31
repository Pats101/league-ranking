import pytest
from src.models.team import Team

@pytest.fixture
def team():
    return Team("Lions")

def test_new_team_starts_empty(team):
    assert team.name == "Lions"
    assert team.points == team.wins == team.draws == team.losses == 0

def test_win_adds_three_points(team):
    team.add_win()
    assert team.points == 3
    assert team.wins == 1

def test_draw_adds_one_point(team):
    team.add_draw()
    assert team.points == 1
    assert team.draws == 1

def test_mixed_results(team):
    team.add_win()
    team.add_draw()
    team.add_loss()
    
    assert team.points == 4
    assert team.wins == team.draws == team.losses == 1

def test_team_ordering():
    lions = Team("Lions")
    snakes = Team("Snakes")
    antelopes = Team("Antelopes")
    
    lions.add_win()      # 3 points
    antelopes.add_win()  # 3 points
    snakes.add_draw()    # 1 point
    
    assert snakes < lions < antelopes