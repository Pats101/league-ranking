import pytest
from src.services.match_ranking_evaluator import MatchRankingEvaluator
from src.models.match import Match
from src.models.team import Team

@pytest.fixture
def matches():
    return [
        Match("Lions", 3, "Snakes", 3),
        Match("Tarantulas", 1, "FC Awesome", 0),
        Match("Lions", 1, "FC Awesome", 1),
        Match("Tarantulas", 3, "Snakes", 1),
        Match("Lions", 4, "Grouches", 0)
    ]

def test_basic_ranking(matches):
    rankings = MatchRankingEvaluator.calculate_rankings(matches)
    
    assert len(rankings) == 5
    assert rankings[0].name == "Tarantulas"
    assert rankings[0].points == 6

def test_empty_list():
    assert len(MatchRankingEvaluator.calculate_rankings([])) == 0

def test_ties():
    matches = [
        Match("Team A", 2, "Team B", 2),
        Match("Team C", 2, "Team D", 2)
    ]
    
    rankings = MatchRankingEvaluator.calculate_rankings(matches)
    
    assert len(rankings) == 4
    assert all(team.points == 1 for team in rankings)
    assert [t.name for t in rankings] == ["Team A", "Team B", "Team C", "Team D"]

def test_win_loss():
    matches = [
        Match("Winners", 3, "Losers", 0),
    ]
    
    rankings = MatchRankingEvaluator.calculate_rankings(matches)
    
    assert len(rankings) == 2
    assert rankings[0].name == "Winners"
    assert rankings[0].points == 3
    assert rankings[1].name == "Losers"
    assert rankings[1].points == 0

def test_complex_scenario():
    matches = [
        Match("Team A", 2, "Team B", 0),  # A wins (3 points)
        Match("Team B", 1, "Team C", 1),  # B & C tie (1 point each)
        Match("Team C", 3, "Team A", 1),  # C wins (3 points)
    ]
    
    rankings = MatchRankingEvaluator.calculate_rankings(matches)
    
    assert len(rankings) == 3
    assert rankings[0].name == "Team C"
    assert rankings[0].points == 4
    assert rankings[1].name == "Team A"
    assert rankings[1].points == 3
    assert rankings[2].name == "Team B"
    assert rankings[2].points == 1

@pytest.mark.parametrize("bad_input", [None, "not a list", [{"not": "a match"}]])
def test_invalid_inputs(bad_input):
    with pytest.raises((TypeError, AttributeError)):
        MatchRankingEvaluator.calculate_rankings(bad_input)