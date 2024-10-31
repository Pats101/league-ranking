# League Ranking System

Hi Span Digital,

My name is Patrick. Thank you for the opportunity to work on this project. A system to help track rankings for a league. The project includes options for both manual input and file-based input. As per the project requirements, I've implemented the ranking system logic. To run the project locally please follow the instructions that will follow.


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

To run the program in non-interactive mode, execute the following command. The program will read match results from the 'matches.txt' file located in the root directory (league-ranking). You can create a new file with your desired match results and replace 'matches.txt' in the command with the new file name. The system will process the results and display them, sorted from highest to lowest with teams sharing the same score listed alphabetically.
Run command:
```bash
python -m src.main matches.txt
```

## Running Program via Terminal

To run the program in interactive mode, execute the following command. Input the match results one by one, pressing Enter after each entry. When finished, type 'done' to calculate and display the results. The results will be sorted from highest to lowest, with teams sharing the same score listed alphabetically.
Run command:
```bash
python -m src.main
```