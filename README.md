# League Ranking System

A system to help track rankings for a soccer league.

## Features
- Calculate league rankings based on match results
- Support for file input and interactive input
- When running file input please run (python -m src.main example.txt)
- Points system: Win (3 points), Draw (1 point), Loss (0 points)
- Handles ties with alphabetical ordering

## Requirements
- Python 3.8+
- pip (Python package installer)

## Installation

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Development

Install development dependencies:
```bash
pip install -e .
```

## Testing

Run tests:
```bash
python -m pytest
```

## Running Program with Example txt file in project root

Run tests:
```bash
python -m src.main matches.txt
```