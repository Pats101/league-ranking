from .services.game_data_analyzer import GameDataAnalyzer
from .services.league_service import LeagueService
import sys
import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def process_matches(lines, parser, league):
    """Process matches from a list of lines"""
    for line in lines:
        if line.strip():
            match = parser.parse_line(line.strip())
            league.process_match(match)

def print_rankings(rankings):
    """Print the rankings in the required format"""
    for rank, team, points in rankings:
        points_label = "pt" if points == 1 else "pts"
        print(f"{rank}. {team}, {points} {points_label}")

def read_from_stdin():
    """Read match results from stdin until user types 'done'"""
    print("Enter match results (one per line).")
    print("Type 'done' to finish entering results.")
    
    lines = []
    while True:
        line = input().strip()
        if line.lower() == 'done':
            break
        if line:
            lines.append(line)
    return lines

def main():
    parser = GameDataAnalyzer()
    league = LeagueService()

    try:
        if len(sys.argv) > 1:
            logger.info(f"Reading matches from file: {sys.argv[1]}")
            with open(sys.argv[1], 'r') as file:
                process_matches(file, parser, league)
        else:
            logger.info("Reading matches from stdin")
            process_matches(read_from_stdin(), parser, league)

        print_rankings(league.get_rankings())
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()