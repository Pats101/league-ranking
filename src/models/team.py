from dataclasses import dataclass

@dataclass
class Team:
    def __init__(self, name: str):
        self.name = name
        self.points = 0
        self.matches_played = 0
        self.wins = 0
        self.draws = 0
        self.losses = 0

    def add_win(self):
        self.wins += 1
        self.points += 3
        self.matches_played += 1

    def add_draw(self):
        self.draws += 1
        self.points += 1
        self.matches_played += 1

    def add_loss(self):
        self.losses += 1
        self.matches_played += 1

    def add_points(self, points: int) -> None:
        """Add points to the team's total points.
        
        Args:
            points (int): The number of points to add
        """
        self.points += points

    def __eq__(self, other):
        if not isinstance(other, Team):
            return NotImplemented
        return self.name == other.name and self.points == other.points

    def __lt__(self, other):
        if not isinstance(other, Team):
            return NotImplemented
        # First compare by points (descending)
        if self.points != other.points:
            return self.points < other.points
        # If points are equal, compare by name (ascending)
        return self.name < other.name

    def __gt__(self, other):
        if not isinstance(other, Team):
            return NotImplemented
        # First compare by points (descending)
        if self.points != other.points:
            return self.points > other.points
        # If points are equal, compare by name (ascending)
        return self.name > other.name

    def __str__(self):
        return f"Team(name='{self.name}', points={self.points}, wins={self.wins}, draws={self.draws}, losses={self.losses})"

    def __repr__(self):
        return self.__str__()