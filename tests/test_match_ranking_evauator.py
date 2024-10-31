import pytest
from src.services.match_ranking_evaluator import MatchRankingEvaluator
from src.models.match import Match
from src.models.team import Team

@pytest.fixture
def sample_matches():
    return [
        Match("Lions", 3, "Snakes", 3),
        Match("Tarantulas", 1, "FC Awesome", 0),
        Match("Lions", 1, "FC Awesome", 1),
        Match("Tarantulas", 3, "Snakes", 1),
        Match("Lions", 4, "Grouches", 0)
    ]

def test_calculate_rankings_basic(sample_matches):
    # Act
    rankings = MatchRankingEvaluator.calculate_rankings(sample_matches)
    
    # Assert
    assert len(rankings) == 5  # 5 unique teams
    assert isinstance(rankings[0], Team)
    
    # Verify correct order (Tarantulas should be first with 6 points)
    assert rankings[0].name == "Tarantulas"
    assert rankings[0].points == 6

def test_calculate_rankings_empty_list():
    # Act
    rankings = MatchRankingEvaluator.calculate_rankings([])
    
    # Assert
    assert len(rankings) == 0
    assert isinstance(rankings, list)

def test_calculate_rankings_tie_scenario():
    matches = [
        Match("Team A", 2, "Team B", 2),
        Match("Team C", 2, "Team D", 2)
    ]
    
    # Act
    rankings = MatchRankingEvaluator.calculate_rankings(matches)
    
    # Assert
    assert len(rankings) == 4
    # All teams should have 1 point (for a tie)
    assert all(team.points == 1 for team in rankings)
    # Teams should be in alphabetical order when points are equal
    team_names = [team.name for team in rankings]
    assert team_names == sorted(team_names)

def test_calculate_rankings_win_loss_scenario():
    matches = [
        Match("Winners", 3, "Losers", 0),
    ]
    
    # Act
    rankings = MatchRankingEvaluator.calculate_rankings(matches)
    
    # Assert
    assert len(rankings) == 2
    assert rankings[0].name == "Winners"
    assert rankings[0].points == 3
    assert rankings[1].name == "Losers"
    assert rankings[1].points == 0

def test_calculate_rankings_complex_scenario():
    matches = [
        Match("Team A", 2, "Team B", 0),  # A wins (3 points)
        Match("Team B", 1, "Team C", 1),  # B & C tie (1 point each)
        Match("Team C", 3, "Team A", 1),  # C wins (3 points)
    ]
    
    # Act
    rankings = MatchRankingEvaluator.calculate_rankings(matches)
    
    # Assert
    assert len(rankings) == 3
    # Team C should be first (4 points total)
    assert rankings[0].name == "Team C"
    assert rankings[0].points == 4
    # Team A should be second (3 points)
    assert rankings[1].name == "Team A"
    assert rankings[1].points == 3
    # Team B should be last (1 point)
    assert rankings[2].name == "Team B"
    assert rankings[2].points == 1

@pytest.mark.parametrize("match_data", [
    None,
    "not a list",
    [{"not": "a match object"}]
])
def test_calculate_rankings_invalid_input(match_data):
    # Assert
    with pytest.raises((TypeError, AttributeError)):
        MatchRankingEvaluator.calculate_rankings(match_data)