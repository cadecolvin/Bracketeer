from json import JSONEncoder


class Round(object):
    """
    Represents a round in the tournament. A round consists of the four
    regions.
    """
    def __init__(self, round_number):
        self.number = round_number
        self.regions = []


class Region(object):
    """
    Represents a region of play in the tournament. This is how teams
    are organized and seeded within the bracket.
    """
    def __init__(self):
        self.games = []


class Game(object):
    """
    Represents a game in the tournament. Has two teams and will 
    determine a winner.
    """
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2

    def play(self):
        """Returns a winning team based on the teams odds"""
        if self.team1.get_odds() > self.team2.get_odds():
            return self.team1
        else:
            return self.team2


class Team(object):
    """
    Represents a team in the tournament. A team will have a name,
    wins, and a seed. The wins should be represented as the number of wins
    less the number of losses. eg. A record of 22-12 is 10 wins.
    """
    def __init__(self, name, wins, seed):
        self.name = name
        self.wins = int(wins)
        self.seed = int(seed)

    def __str__(self):
        return self.name

    def get_odds(self):
        """Returns the teams odds of winning based on seed and wins"""
        seed_weight = 0.6
        win_weight = 0.4

        seed_factor = (17 - self.seed) * seed_weight
        win_factor = self.wins * win_weight

        return seed_factor + win_factor
