# League Ranking System

A simple system for tracking league rankings based on match results. Supports both file input and interactive command-line input.

## Quick Start

```bash
# Set up your environment
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt

# Run with a file
python -m src.main matches.txt

# Or run interactively
python -m src.main
```

## How It Works

- Teams get 3 points for a win, 1 for a draw, 0 for a loss
- Tied teams are sorted alphabetically
- Input match results one at a time or via a text file
- Format: `Team A 3, Team B 0`

## Development

```bash
# Install dev dependencies
pip install -e .

# Run tests
python -m pytest
```

## Requirements

- Python 3.8+